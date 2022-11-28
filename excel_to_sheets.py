import os
import pandas as pd

cwd = os.path.abspath('gnews_4')  # change file path
files = os.listdir(cwd)
files.sort()

df = pd.DataFrame()
df.to_excel('google_news_4.xlsx', sheet_name='3M', index=False)  # change excel file name

for file in files:
    print(file)
    if file.endswith('.xlsx'):

        sheet_name = file.split('_')[0]
        df_excel = pd.read_excel('gnews_4/'+file)  # change file path

        # change excel file name
        with pd.ExcelWriter("google_news_4.xlsx", mode='a', if_sheet_exits='replace') as writer:

            df_excel.to_excel(writer, sheet_name=sheet_name, index=False)
