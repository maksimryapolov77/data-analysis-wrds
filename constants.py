cik_aaers = 'math_init_data\\cik_aaers.csv'
cik_gao = 'math_init_data\\cik_gao.csv'
cik_res = 'math_init_data\\cik_res.csv'
cik_sec2 = 'math_init_data\\cik_sec2.csv'

cik_list = [
    cik_aaers,
    cik_gao,
    cik_res,
    cik_sec2,
]

init_aaers = 'math_init_data\\merged_init_matching_aaers.csv'
init_gao = 'math_init_data\\merged_init_matching_gao.csv'
init_res = 'math_init_data\\merged_init_matching_res.csv'
init_sec2 = 'math_init_data\\merged_init_matching_sec2.csv'

init_data_list = [
    init_aaers,
    init_gao,
    init_res,
    init_sec2,
]

target_col = 'Total Periods'
cik_col = 'CIK Code'
ticker_col = 'Ticker Symbol'
index_col = 'datadate'

data_set_aaers = 'math_init_data\\data_set_aaers.csv'
data_set_gao = 'math_init_data\\data_set_gao.csv'
data_set_res = 'math_init_data\\data_set_res.csv'
data_set_sec2 = 'math_init_data\\data_set_sec2.csv'

data_set_list = [
    data_set_aaers,
    data_set_gao,
    data_set_res,
    data_set_sec2,
]

parsed_aaers = 'math_init_data\\parsed_aaers.csv'
parsed_gao = 'math_init_data\\parsed_gao.csv'
parsed_res = 'math_init_data\\parsed_res.csv'
parsed_sec2 = 'math_init_data\\parsed_sec2.csv'

parsed_list = [
    parsed_aaers,
    parsed_gao,
    parsed_res,
    parsed_sec2,
]

merged_e_aaers = 'D:\\src\\python\\ravenpack\\e_combine\\merged_e_aaers.csv'
merged_e_gao = 'D:\\src\\python\\ravenpack\\e_combine\\merged_e_gao.csv'
merged_e_restatement = 'D:\\src\\python\\ravenpack\\e_combine\\merged_e_restatement.csv'
merged_e_sec2 = 'D:\\src\\python\\ravenpack\\e_combine\\merged_e_sec2.csv'

merged_e_list = [
    merged_e_aaers,
    merged_e_gao,
    merged_e_restatement,
    merged_e_sec2,
]

result_aaers = 'math_init_data\\result_aaers.csv'
result_gao = 'math_init_data\\result_gao.csv'
result_restatement = 'math_init_data\\result_restatement.csv'
result_sec2 = 'math_init_data\\result_sec2.csv'

result_list = [
    result_aaers,
    result_gao,
    result_restatement,
    result_sec2,
]
limit_date = 20190331
exception_year = 2018
limit_year = 2019
start_year = 2000

default_columns = ['COMPANY NAME', 'CIK', 'CUSIP', 'CUSIP_8D', 'CUSIP_9D', 'TICKER',
                   'RP_Entity_ID_1', 'RP_Entity_ID_2', 'RP_Entity_ID_3', 'RP_Entity_ID_4', 'RP_Entity_ID_5']

additional_columns = [
    'CIK2',
    'TICKER2',
    'Starting_Date',
    'Ending_Date',
    'Total news articles all Fiscal Periods',

    'Data Date 2000',
    'Fiscal Year endmonth 2000',
    'Current Assets - Total 2000',
    'Cash and Short-Term Investments 2000',
    'Current Liabilities - Total 2000',
    'Commercial Paper 2000',
    'Notes Payable 2000',
    'Revenue 2000',
    'Total Articles 2000-2001',

    'Data Date 2001',
    'Fiscal Year endmonth 2001',
    'Current Assets - Total 2001',
    'Cash and Short-Term Investments 2001',
    'Current Liabilities - Total 2001',
    'Commercial Paper 2001',
    'Notes Payable 2001',
    'Revenue 2001',
    'Abnormal Accrual 2001 (AWCAt)',
    'Control Variable 1 - 2001',
    'Control Variable 2 - 2001',
    'Control Variable 3 - 2001',
    'Control Variable 4 - 2001',
    'Control Variable 5 - 2001',
    'Control Variable 6 - 2001',
    'Total Articles 2001-2002',
    
    'Data Date 2002',
    'Fiscal Year endmonth 2002',
    'Current Assets - Total 2002',
    'Cash and Short-Term Investments 2002',
    'Current Liabilities - Total 2002',
    'Commercial Paper 2002',
    'Notes Payable 2002',
    'Revenue 2002',
    'Abnormal Accrual 2002 (AWCAt)',
    'Control Variable 1 - 2002',
    'Control Variable 2 - 2002',
    'Control Variable 3 - 2002',
    'Control Variable 4 - 2002',
    'Control Variable 5 - 2002',
    'Control Variable 6 - 2002',
    'Total Articles 2002-2003',

    'Data Date 2003',
    'Fiscal Year endmonth 2003',
    'Current Assets - Total 2003',
    'Cash and Short-Term Investments 2003',
    'Current Liabilities - Total 2003',
    'Commercial Paper 2003',
    'Notes Payable 2003',
    'Revenue 2003',
    'Abnormal Accrual 2003 (AWCAt)',
    'Control Variable 1 - 2003',
    'Control Variable 2 - 2003',
    'Control Variable 3 - 2003',
    'Control Variable 4 - 2003',
    'Control Variable 5 - 2003',
    'Control Variable 6 - 2003',
    'Total Articles 2003-2004',

    'Data Date 2004',
    'Fiscal Year endmonth 2004',
    'Current Assets - Total 2004',
    'Cash and Short-Term Investments 2004',
    'Current Liabilities - Total 2004',
    'Commercial Paper 2004',
    'Notes Payable 2004',
    'Revenue 2004',
    'Abnormal Accrual 2004 (AWCAt)',
    'Control Variable 1 - 2004',
    'Control Variable 2 - 2004',
    'Control Variable 3 - 2004',
    'Control Variable 4 - 2004',
    'Control Variable 5 - 2004',
    'Control Variable 6 - 2004',
    'Total Articles 2004-2005',

    'Data Date 2005',
    'Fiscal Year endmonth 2005',
    'Current Assets - Total 2005',
    'Cash and Short-Term Investments 2005',
    'Current Liabilities - Total 2005',
    'Commercial Paper 2005',
    'Notes Payable 2005',
    'Revenue 2005',
    'Abnormal Accrual 2005 (AWCAt)',
    'Control Variable 1 - 2005',
    'Control Variable 2 - 2005',
    'Control Variable 3 - 2005',
    'Control Variable 4 - 2005',
    'Control Variable 5 - 2005',
    'Control Variable 6 - 2005',
    'Total Articles 2005-2006',

    'Data Date 2006',
    'Fiscal Year endmonth 2006',
    'Current Assets - Total 2006',
    'Cash and Short-Term Investments 2006',
    'Current Liabilities - Total 2006',
    'Commercial Paper 2006',
    'Notes Payable 2006',
    'Revenue 2006',
    'Abnormal Accrual 2006 (AWCAt)',
    'Control Variable 1 - 2006',
    'Control Variable 2 - 2006',
    'Control Variable 3 - 2006',
    'Control Variable 4 - 2006',
    'Control Variable 5 - 2006',
    'Control Variable 6 - 2006',
    'Total Articles 2006-2007',

    'Data Date 2007',
    'Fiscal Year endmonth 2007',
    'Current Assets - Total 2007',
    'Cash and Short-Term Investments 2007',
    'Current Liabilities - Total 2007',
    'Commercial Paper 2007',
    'Notes Payable 2007',
    'Revenue 2007',
    'Abnormal Accrual 2007 (AWCAt)',
    'Control Variable 1 - 2007',
    'Control Variable 2 - 2007',
    'Control Variable 3 - 2007',
    'Control Variable 4 - 2007',
    'Control Variable 5 - 2007',
    'Control Variable 6 - 2007',
    'Total Articles 2007-2008',

    'Data Date 2008',
    'Fiscal Year endmonth 2008',
    'Current Assets - Total 2008',
    'Cash and Short-Term Investments 2008',
    'Current Liabilities - Total 2008',
    'Commercial Paper 2008',
    'Notes Payable 2008',
    'Revenue 2008',
    'Abnormal Accrual 2008 (AWCAt)',
    'Control Variable 1 - 2008',
    'Control Variable 2 - 2008',
    'Control Variable 3 - 2008',
    'Control Variable 4 - 2008',
    'Control Variable 5 - 2008',
    'Control Variable 6 - 2008',
    'Total Articles 2008-2009',

    'Data Date 2009',
    'Fiscal Year endmonth 2009',
    'Current Assets - Total 2009',
    'Cash and Short-Term Investments 2009',
    'Current Liabilities - Total 2009',
    'Commercial Paper 2009',
    'Notes Payable 2009',
    'Revenue 2009',
    'Abnormal Accrual 2009 (AWCAt)',
    'Control Variable 1 - 2009',
    'Control Variable 2 - 2009',
    'Control Variable 3 - 2009',
    'Control Variable 4 - 2009',
    'Control Variable 5 - 2009',
    'Control Variable 6 - 2009',
    'Total Articles 2009-2010',

    'Data Date 2010',
    'Fiscal Year endmonth 2010',
    'Current Assets - Total 2010',
    'Cash and Short-Term Investments 2010',
    'Current Liabilities - Total 2010',
    'Commercial Paper 2010',
    'Notes Payable 2010',
    'Revenue 2010',
    'Abnormal Accrual 2010 (AWCAt)',
    'Control Variable 1 - 2010',
    'Control Variable 2 - 2010',
    'Control Variable 3 - 2010',
    'Control Variable 4 - 2010',
    'Control Variable 5 - 2010',
    'Control Variable 6 - 2010',
    'Total Articles 2010-2011',

    'Data Date 2011',
    'Fiscal Year endmonth 2011',
    'Current Assets - Total 2011',
    'Cash and Short-Term Investments 2011',
    'Current Liabilities - Total 2011',
    'Commercial Paper 2011',
    'Notes Payable 2011',
    'Revenue 2011',
    'Abnormal Accrual 2011 (AWCAt)',
    'Control Variable 1 - 2011',
    'Control Variable 2 - 2011',
    'Control Variable 3 - 2011',
    'Control Variable 4 - 2011',
    'Control Variable 5 - 2011',
    'Control Variable 6 - 2011',
    'Total Articles 2011-2012',

    'Data Date 2012',
    'Fiscal Year endmonth 2012',
    'Current Assets - Total 2012',
    'Cash and Short-Term Investments 2012',
    'Current Liabilities - Total 2012',
    'Commercial Paper 2012',
    'Notes Payable 2012',
    'Revenue 2012',
    'Abnormal Accrual 2012 (AWCAt)',
    'Control Variable 1 - 2012',
    'Control Variable 2 - 2012',
    'Control Variable 3 - 2012',
    'Control Variable 4 - 2012',
    'Control Variable 5 - 2012',
    'Control Variable 6 - 2012',
    'Total Articles 2012-2013',

    'Data Date 2013',
    'Fiscal Year endmonth 2013',
    'Current Assets - Total 2013',
    'Cash and Short-Term Investments 2013',
    'Current Liabilities - Total 2013',
    'Commercial Paper 2013',
    'Notes Payable 2013',
    'Revenue 2013',
    'Abnormal Accrual 2013 (AWCAt)',
    'Control Variable 1 - 2013',
    'Control Variable 2 - 2013',
    'Control Variable 3 - 2013',
    'Control Variable 4 - 2013',
    'Control Variable 5 - 2013',
    'Control Variable 6 - 2013',
    'Total Articles 2013-2014',

    'Data Date 2014',
    'Fiscal Year endmonth 2014',
    'Current Assets - Total 2014',
    'Cash and Short-Term Investments 2014',
    'Current Liabilities - Total 2014',
    'Commercial Paper 2014',
    'Notes Payable 2014',
    'Revenue 2014',
    'Abnormal Accrual 2014 (AWCAt)',
    'Control Variable 1 - 2014',
    'Control Variable 2 - 2014',
    'Control Variable 3 - 2014',
    'Control Variable 4 - 2014',
    'Control Variable 5 - 2014',
    'Control Variable 6 - 2014',
    'Total Articles 2014-2015',

    'Data Date 2015',
    'Fiscal Year endmonth 2015',
    'Current Assets - Total 2015',
    'Cash and Short-Term Investments 2015',
    'Current Liabilities - Total 2015',
    'Commercial Paper 2015',
    'Notes Payable 2015',
    'Revenue 2015',
    'Abnormal Accrual 2015 (AWCAt)',
    'Control Variable 1 - 2015',
    'Control Variable 2 - 2015',
    'Control Variable 3 - 2015',
    'Control Variable 4 - 2015',
    'Control Variable 5 - 2015',
    'Control Variable 6 - 2015',
    'Total Articles 2015-2016',

    'Data Date 2016',
    'Fiscal Year endmonth 2016',
    'Current Assets - Total 2016',
    'Cash and Short-Term Investments 2016',
    'Current Liabilities - Total 2016',
    'Commercial Paper 2016',
    'Notes Payable 2016',
    'Revenue 2016',
    'Abnormal Accrual 2016 (AWCAt)',
    'Control Variable 1 - 2016',
    'Control Variable 2 - 2016',
    'Control Variable 3 - 2016',
    'Control Variable 4 - 2016',
    'Control Variable 5 - 2016',
    'Control Variable 6 - 2016',
    'Total Articles 2016-2017',

    'Data Date 2017',
    'Fiscal Year endmonth 2017',
    'Current Assets - Total 2017',
    'Cash and Short-Term Investments 2017',
    'Current Liabilities - Total 2017',
    'Commercial Paper 2017',
    'Notes Payable 2017',
    'Revenue 2017',
    'Abnormal Accrual 2017 (AWCAt)',
    'Control Variable 1 - 2017',
    'Control Variable 2 - 2017',
    'Control Variable 3 - 2017',
    'Control Variable 4 - 2017',
    'Control Variable 5 - 2017',
    'Control Variable 6 - 2017',
    'Total Articles 2017-2018',

    'Data Date 2018',
    'Fiscal Year endmonth 2018',
    'Current Assets - Total 2018',
    'Cash and Short-Term Investments 2018',
    'Current Liabilities - Total 2018',
    'Commercial Paper 2018',
    'Notes Payable 2018',
    'Revenue 2018',
    'Abnormal Accrual 2018 (AWCAt)',
    'Control Variable 1 - 2018',
    'Control Variable 2 - 2018',
    'Control Variable 3 - 2018',
    'Control Variable 4 - 2018',
    'Control Variable 5 - 2018',
    'Control Variable 6 - 2018',
    'Total Articles 2018-2019',

    'Data Date 2019',
    'Fiscal Year endmonth 2019',
    'Current Assets - Total 2019',
    'Cash and Short-Term Investments 2019',
    'Current Liabilities - Total 2019',
    'Commercial Paper 2019',
    'Notes Payable 2019',
    'Revenue 2019',
    'Abnormal Accrual 2019 (AWCAt)',
    'Control Variable 1 - 2019',
    'Control Variable 2 - 2019',
    'Control Variable 3 - 2019',
    'Control Variable 4 - 2019',
    'Control Variable 5 - 2019',
    'Control Variable 6 - 2019',
]