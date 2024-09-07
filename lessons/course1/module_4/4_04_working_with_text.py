import pandas as pd

from lessons.course1.module_4.data_frame import df_csv

df = pd.DataFrame({'Column':['Hello','World','Python','Data Science']})

df['Length'] = df['Column'].str.len()
print('Length of each string:')
print(df[['Column','Length']])
print(df)