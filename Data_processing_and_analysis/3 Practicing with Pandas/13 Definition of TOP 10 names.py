# Определить ТОП 10 имен
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\3 Practicing with Pandas\11 result.csv')
print(df)

# Взять топ 10 женских и топ 10 мужских имён за всё время с 1880 по 2019

# df2 = df.groupby('Name').sum()['Cnt']
# print(df2)

# print(df2.loc[ (df2.index.get_level_values(0).isin(range(2010, 2020))) & (df2.index.get_level_values(1) == 'F')])

# Топ 10 мальчиков за всё время
df_male = df[ df.Sex == 'M' ].groupby('Name').sum()
print(df_male.sort_values('Cnt', ascending=False).head(10))
# Топ 10 девочек за всё время
df_female = df[ df.Sex == 'F' ].groupby('Name').sum()
print(df_female.sort_values('Cnt', ascending=False).head(10))

# 10 популярных женских имён без дублей
# print(df[ df.Sex == 'F'].sort_values('Cnt', ascending=False))
df_f_top = df[ df.Sex == 'F'].sort_values('Cnt', ascending=False).drop_duplicates(subset=['Name']).head(10)
print(df_f_top)

# print(df[ df.Sex == 'M'].sort_values('Cnt', ascending=False))
df_m_top = df[ df.Sex == 'M'].sort_values('Cnt', ascending=False).drop_duplicates(subset=['Name']).head(10)
print(df_m_top)


# Удалить дубли имён и годов
# df_m_top2 = df[ df.Sex == 'M'].sort_values('Cnt', ascending=False).drop_duplicates(subset=['Name'])\
# .drop_duplicates(subset=['Year']).head(10)
# print(df_m_top2)


df_all = pd.concat([df_m_top, df_f_top])
print(df_all)