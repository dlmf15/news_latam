import pandas as pd
import numpy as np

df = pd.read_csv('/Users/devalou/PycharmProjects/news_latam/mean_table_all_3days.csv', delimiter=';', usecols=[0, 1, 2, 3, 4])
df = df.replace('#N/A', 0)




df['variance'] = np.var(df[['mean_0907', 'mean_1407', 'mean_1507']], axis=1)
df['std'] = np.std(df[['mean_0907', 'mean_1407', 'mean_1507']], axis=1)
df.to_excel('variance_std_table.xlsx')
print(df)



