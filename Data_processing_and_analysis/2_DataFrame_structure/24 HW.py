# Объединение таблиц с merge и join
import pandas as pd
# HW
# Объедините таблицы городов и стран, добавив к таблице городов наименование страны.
# В итоговом дата фрейме должны быть следующие столбцы:
# • ID (ID города)
# • City (Название города)
# • CountryCode (Код страны)
# • Country (Название страны)
# • * Population (Кол-во населения города)
# Итоговый датафрейм сохранить в файл Result.xlsx

# 1. 
df_city = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\10 city.csv', sep=';')
print(df_city)

df_country = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\13 country.csv', sep=';')
print(df_country)
# 2. 
df_total = pd.merge(df_city, df_country, how='left', left_on='CountryCode', right_on='Code')\
    [['ID','Name_x', 'CountryCode', 'Name_y', 'Population_x']]

df_total.rename(columns={'Name_x':'City', 'Name_y': 'Country', 'Population_x': 'Population'}, inplace=True)
print(df_total)


df_total.to_excel(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\24 Result.xlsx', index=False)

