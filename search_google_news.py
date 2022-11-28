from datetime import datetime
import pandas as pd
import requests

df = pd.read_csv('/Users/devalou/PycharmProjects/news_latam/mean_table_final.csv', delimiter=';')
# df = pd.read_csv('/Users/devalou/PycharmProjects/news_latam/last_part.csv', delimiter=';')
dfd = df.copy()
#dfd = df[:385]  # 1
#dfd = df[288:385]  # 2
#dfd = df[385:534]  # 3
#dfd = df[534:616]  # 4
#dfd = df[385:]  # 5


def google_search(row_info, file):
    domain = {
               'argentina': 'google.com.ar',
               'bolivia': 'google.com.bo',
               'brazil': 'google.com.br',
               'chile': 'google.cl',
               'colombia': 'google.com.co',
               'ecuador': 'google.com.ec',
               'mexico': 'google.com.mx',
               'peru': 'google.com.pe'
              }

    brand_df = pd.DataFrame(columns=['brand name', 'argentina', 'bolivia', 'brazil', 'chile', 'colombia', 'ecuador',
                                     'mexico', 'peru'])
    brand_name_year = []

    for year in range(13, 21):  # create 'brand_name' column with years
        brand_name_year.append(row_info['brand_name']+'_'+str(year))
    brand_df['brand name'] = brand_name_year

    for country in ['argentina', 'bolivia', 'brazil', 'chile', 'colombia', 'ecuador', 'mexico', 'peru']:

        if country == 'brazil':
            language = 'pt-br'
        else:
            language = 'es'

        if row_info[country] == 'Si':
            query_result = []
            for year in ['2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']:
                params = {
                    'api_key': '',
                    'search_type': 'news',
                    'hl': language,  # language:spanish or portuguese
                    'gl': domain[country].split('.')[-1],  # change

                    #  'location': country,  # change
                    #'google_domain': domain[country],  # change
                    'google_domain': 'google.com',
                    'q': row_info['query'] + ' location:{} before:{}-01-01 after:{}-01-01'.format(country, int(year) + 1
                                                                                                  , year),
                    'output': 'csv',
                    'csv_fields': 'search_information.total_results,search_information.original_query_yields_zero_results'
                }
                api_result = requests.get('https://api.valueserp.com/search', params)
                num_searches = api_result.text.split('\n')[-1].split(',')[0]
                no_result = api_result.text.split('\n')[-1].split(',')[1]
                if no_result == 'true':
                    query_result.append(0)
                    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), country, row_info['brand_name'], year, ': ', 0,
                          file=file)
                    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), country, row_info['brand_name'], year, ': ', 0)

                # elif num_searches == '"search_information.total_results"':  # if didn't get any results
                elif num_searches == '':
                    query_result.append(0)
                    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), country, row_info['brand_name'], year, ': ', 0,
                          file=file)
                    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), country, row_info['brand_name'], year, ': ', 0)
                else:  # turn into int
                    query_result.append(int(num_searches))
                    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), country, row_info['brand_name'], year, ': ',
                          num_searches, file=file)
                    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), country, row_info['brand_name'], year, ': ',
                          num_searches)

            brand_df[country] = query_result
        else:
            brand_df[country] = ['x' for i in range(13, 21)]
            print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), country, row_info['brand_name'], ': ', 'x', file=file)
            print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), country, row_info['brand_name'], ': ', 'x')
    return brand_df


f = open('google_news_log_5_5.txt', 'a')
for name, group in dfd.groupby('company'):

    # print(name)
    result_df = pd.DataFrame(columns=['brand name', 'argentina', 'bolivia', 'brazil', 'chile', 'colombia', 'ecuador',
                                      'mexico', 'peru'])
    for index in range(len(group.index)):
        company = group.iloc[index]['company']
        result_df = pd.concat([result_df, google_search(group.iloc[index], f)])
    # to_excel
    # print(result_df)
    result_df.to_excel('/Users/devalou/PycharmProjects/news_latam/gnews_5/{}_gnews.xlsx'.format(name), sheet_name=name,
                       index=False)
