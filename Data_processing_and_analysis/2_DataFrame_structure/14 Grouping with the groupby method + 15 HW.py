# Группировка методом groupby
import pandas as pd

df = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\10 city.csv', sep=';')
print(df)

# Группировка по стране
# print(df[ df['CountryCode'] =='AFG' ]['Population'].max())
# print(df[ df['CountryCode'] =='AFG' ][['Population', 'District']].max())

# То, по чему группируешь, то является индексом
# print(df.groupby('CountryCode').sum()) # По всем колонкам
# print(df.groupby('CountryCode').sum()['Population']) # По Population, 
# print(df.groupby('CountryCode').agg(['min','max','mean','sum','count'])['Population'].head()) 
# # Как обнулить индексы и выровнять
# print(df.groupby('CountryCode').agg(['min','max','mean','sum','count'])['Population'].reset_index().head()) 

# code_group = df.groupby('CountryCode')
# # Получить данные из одной группы
# print(code_group.get_group('AFG'))

# # Просто тест как работает группировка
# for index, value in code_group:
#     print(index)
#     print(value)

# Получить статитстику (count, mean, std, min, max, 25% ...)
# print(code_group.describe()['Population'])

#  HW ==============================================================
#  1 Сгруппировать данные по CountryCode
# получить максимум и минимум по Population (agg)
# Взять первые 10 результатов
# нормализовать индексы датафрейма (0,1,...9) (На выходе получить датафрейм, а не серию)
print(df)
print(df.groupby('CountryCode').agg(['min', 'max'])['Population'].reset_index().head(10))
# 2 Сгруппировать данные по CountryCode
# получить разницу максимум и минимум по Population (apply)
# Взять первые 10 результатов
# На выходе получить датафрейм, а не серию (нормализовать индексы датафрейма (0,1,...9))
def max_min(row):
    return row['Population'].max() - row['Population'].min()
# Из группы выбрать максимум и минимум
print(df.groupby('CountryCode').apply(lambda row: row['Population'].max() - row['Population'].min()).reset_index().head(10))
print(df.groupby('CountryCode').apply(max_min).reset_index().head(10))
print((df.groupby('CountryCode')['Population'].max() - df.groupby('CountryCode')['Population'].min()).reset_index().head(10))