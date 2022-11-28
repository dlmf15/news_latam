import pandas as pd
import numpy as np
import os

cwd = os.path.abspath('gnews_4')  # change file path
files = os.listdir(cwd)
files.sort()

df = pd.DataFrame(columns=['company', 'brand', 'mean'])

for file in files:
    print(file)
    if file.endswith('.xlsx'):

        sheet_name = file.split('_')[0]
        df_excel = pd.read_excel('gnews_4/'+file)  # change file path
        #print(df_excel)
        df_excel['year'] = df_excel['brand name'].str.split('_').str[-1]
        df_excel['brand'] = df_excel['brand name'].str.split('_').str[0]
        df_excel = df_excel.replace('x', np.nan)
        df_excel['mean'] = df_excel[['argentina', 'bolivia', 'brazil', 'chile', 'colombia', 'ecuador', 'mexico', 'peru']].mean(axis=1, skipna=True)
        #print(df_excel)
        table = pd.pivot_table(df_excel[['year', 'brand', 'mean']], values='mean', index='year', columns='brand')
        sort_table = table.mean(axis=0).sort_values(ascending=False).to_frame().reset_index().rename(columns={'brand': 'brand', 0: 'mean'})
        sort_table['company'] = sheet_name
        sort_table = sort_table[['company', 'brand', 'mean']]
        print(sort_table)
        df = df.append(sort_table, ignore_index=True)
        print(df)

df.to_excel('mean_table_gn_4.xlsx', index=False)

