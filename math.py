import math
import numpy as np
from pathlib import Path
import constants
import pandas as pd
from time import sleep

useful_df_list = []
def remove_columns():
    for idx, init_data in enumerate(constants.init_data_list):
        df_init_data = pd.read_csv(init_data, low_memory=False)
        if idx is not 1:
            df_init_data[df_init_data[constants.cik_col].notnull()][constants.cik_col].astype(int).to_csv(constants.cik_list[idx], header=False, index=None)
        else:
            df_init_data[df_init_data[constants.ticker_col].notnull()][constants.ticker_col].to_csv(constants.cik_list[idx], header=False, index=None)
        column_list = df_init_data.columns
        target_index = column_list.get_loc(constants.target_col)
        useful_columns = column_list[:target_index]
        useful_df_list.append(df_init_data[useful_columns])
        pass

def parsing_data_set(group, parsed_file):
    df_parsed = pd.DataFrame(columns=constants.additional_columns)
    group = group.set_index(constants.index_col)
    group_index_list = [int(str(index)[0:4]) for index in group.index]
    data_date_dict = dict(zip(group_index_list, group.index))
    for index, year in enumerate(data_date_dict):
        if index == 0:
            start_date = str(data_date_dict.get(year))
            df_parsed.Starting_Date = [start_date]
        if index == len(data_date_dict) -1:
            if year == constants.limit_year:
                if int(data_date_dict.get(year)) > constants.limit_date:
                    end_date = str(data_date_dict.get(constants.exception_year))
                else:
                    end_date = str(data_date_dict.get(year))
            else:
                end_date = str(data_date_dict.get(year))
            # Ending_Date field
            df_parsed.Ending_Date = [end_date]

        index_value = data_date_dict.get(year)
        if parsed_file != constants.parsed_gao:
            # CIK2 field
            cik = group.at[index_value, 'cik']
        else:
            # TICKER2 field
            ticker = group.at[index_value, 'tic']
        # Data Date xxxx field
        data_date = index_value
        # Fiscal Year endmonth xxxx field
        fiscal_year_end_month = str(data_date)[4:6]
        # Current Assets - Total xxxx
        current_asserts_total = group.at[index_value, 'act']
        # Cash and Short-Term Investments xxxx
        cash_and_short_term_investments = group.at[index_value, 'che']
        # Current Liabilities - Total xxxx
        current_liabilities = group.at[index_value, 'lct']
        # Commercial Paper xxxx
        commercial_paper = group.at[index_value, 'cmp']
        # Notes Payable 2000
        notes_payable = group.at[index_value, 'np']
        # Revenue
        revenue = group.at[index_value, 'revt']

        if parsed_file != constants.parsed_gao:
            df_parsed['CIK2'] = [cik]
        else:
            df_parsed['TICKER2'] = [ticker]
        df_parsed['Fiscal Year endmonth ' + str(year)] = [fiscal_year_end_month]
        df_parsed['Current Assets - Total ' + str(year)] = [current_asserts_total]
        if year == constants.limit_year:
            if data_date > constants.limit_date:
                data_date = data_date_dict.get(constants.exception_year)
        df_parsed['Data Date ' + str(year)] = [data_date]
        df_parsed['Cash and Short-Term Investments ' + str(year)] = [cash_and_short_term_investments]
        df_parsed['Current Liabilities - Total ' + str(year)] = [current_liabilities]
        df_parsed['Commercial Paper ' + str(year)] = [commercial_paper]
        df_parsed['Notes Payable ' + str(year)] = [notes_payable]
        df_parsed['Revenue ' + str(year)] = [revenue]

    if not Path(parsed_file).exists():
        df_parsed.to_csv(parsed_file,
                        mode='w', header=True, index=None)
    else:
        df_parsed.to_csv(parsed_file,
                        mode='a', header=False, index=None)
    
    
def split_data_set():
    for idx, (data_set, parsed_file, init_file, merged_file) in enumerate(zip(constants.data_set_list, constants.parsed_list, constants.init_data_list, constants.merged_e_list)):
        df_data_set = pd.read_csv(data_set, low_memory=False)
        if idx != 1:
            grouped = df_data_set.groupby('cik')
        if idx == 1:
            grouped = df_data_set.groupby('tic')
        grouped.apply(parsing_data_set, parsed_file=parsed_file)

        df_parsed_file = pd.read_csv(parsed_file)
        df_init_file = pd.read_csv(init_file, low_memory=False).sort_values(['CIK'])
        if idx == 1:
            df_result = pd.merge(useful_df_list[idx], df_parsed_file, left_on='TICKER',
                            right_on='TICKER2', how='left').drop(['TICKER2', 'CIK2'], axis=1).sort_values(['CIK'])
        else:
            df_result = pd.merge(useful_df_list[idx], df_parsed_file, left_on='CIK',
                            right_on='CIK2', how='left').drop(['CIK2', 'TICKER2'], axis=1).sort_values(['CIK'])

        for year in range(2001, 2020):
            df_result['Control Variable 1 - ' + str(year)] = df_init_file['Control Variable 1 (' + str(year) + ')']
            df_result['Control Variable 2 - ' + str(year)] = df_init_file['Control Variable 2 (' + str(year) + ')']
            df_result['Control Variable 3 - ' + str(year)] = df_init_file['Control Variable 3 (' + str(year) + ')']
            df_result['Control Variable 4 - ' + str(year)] = df_init_file['Control Variable 4 (' + str(year) + ')']
            df_result['Control Variable 5 - ' + str(year)] = df_init_file['Control Variable 5 (' + str(year) + ')']
            df_result['Control Variable 6 - ' + str(year)] = df_init_file['Control Variable 6 (' + str(year) + ')']

        col_list = [col for col in df_result.columns if 'Total news articles fiscal year ' in col]
        df_m = pd.read_csv(merged_file, low_memory=False)
        df_result_not_null = df_result[df_result.Starting_Date.notnull()]
        for index, row in df_result_not_null.iterrows():
            if row.Starting_Date is not np.nan:
                start_date = row.Starting_Date
                end_date = row.Ending_Date

                rps_list = []
                for rp in constants.default_columns[6:11]:
                    if row[rp] is not np.nan:
                        rps_list.append(row[rp])
                df_m_1 = df_m.loc[df_m.RP_ENTITY_ID.isin(rps_list)]
                df_m_2 = df_m_1.loc[(int(start_date) < df_m_1.RPNA_DATE_UTC) & (df_m_1.RPNA_DATE_UTC <= int(end_date))]
                total_count = len(df_m_2.index)
                df_result.set_value(index, 'Total news articles all Fiscal Periods', total_count)

                for year in range(int(str(start_date)[:4]), int(str(end_date)[:4]) + 1):
                    if constants.limit_year > year:
                        start_date_value = row['Data Date ' + str(year)]
                        end_date_value = row['Data Date ' + str(year + 1)]
                        
                        df_m_3 = df_m_1.loc[(df_m_1.RPNA_DATE_UTC > start_date_value) & (df_m_1.RPNA_DATE_UTC <= end_date_value)]
                        year_title = 'Total Articles ' + str(year) + '-' + str(year + 1)
                        df_result.set_value(index, year_title, len(df_m_3.index))

                        if year > constants.start_year:
                            current_assets = row['Current Assets - Total ' + str(year)]
                            current_assets_i = row['Current Assets - Total ' + str(year - 1)]

                            cash_short_term = row['Cash and Short-Term Investments ' + str(year)]
                            cash_short_term_i = row['Cash and Short-Term Investments ' + str(year - 1)]

                            current_liabilities = row['Current Liabilities - Total ' + str(year)]
                            current_liabilities_i = row['Current Liabilities - Total ' + str(year - 1)]

                            commercial_paper = row['Commercial Paper ' + str(year)]
                            commercial_paper_i = row['Commercial Paper ' + str(year - 1)]

                            notes_payable = row['Notes Payable ' + str(year)]
                            notes_payable_i = row['Notes Payable ' + str(year - 1)]

                            if math.isnan(current_assets):
                                current_assets = 0
                            if math.isnan(current_assets_i):
                                current_assets_i = 0
                            if math.isnan(cash_short_term):
                                cash_short_term = 0
                            if math.isnan(cash_short_term_i):
                                cash_short_term_i = 0
                            if math.isnan(current_liabilities):
                                current_liabilities = 0
                            if math.isnan(current_liabilities_i):
                                current_liabilities_i = 0
                            if math.isnan(commercial_paper):
                                commercial_paper = 0
                            if math.isnan(commercial_paper_i):
                                commercial_paper_i = 0
                            if math.isnan(notes_payable):
                                notes_payable = 0
                            if math.isnan(notes_payable_i):
                                notes_payable = 0


                            wct = (current_assets - cash_short_term) - (current_liabilities - (commercial_paper + notes_payable))
                            wc_t = (current_assets_i - cash_short_term_i) - (current_liabilities_i - (commercial_paper_i + notes_payable_i))

                            st = row['Revenue ' + str(year)]
                            s_t = row['Revenue ' + str(year - 1)]

                            if math.isnan(wc_t) or wc_t == 0 or math.isnan(s_t) or s_t == 0 or math.isnan(st) or st == 0:
                                awcat = wct
                            else:
                                awcat = wct - (wc_t / s_t) * st
                            awcat_field = 'Abnormal Accrual ' + str(year) + ' (AWCAt)'
                            df_result.set_value(index, awcat_field, awcat)
        df_result.to_csv(constants.result_list[idx], header=True, index=None)
        print(f'{constants.result_list[idx]} finished')


if __name__ == "__main__":
    remove_columns()
    split_data_set()
    pass