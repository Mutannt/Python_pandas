# Объединение таблиц с merge и join
import pandas as pd

# LEFT JOIN из левой таблицы всё, а из правой если id совпадает

df_products = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\23 products.csv', sep=';')
print(df_products)

df_brands = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\23 brands.csv', sep=';')
print(df_brands)

# Метод merge (соединение объединении на основании колонок)
# how: str = 'inner' (тип объединения)
# lenf_on - по какому ключу

# df_products.merge(df_brands) # (вызывающий датафрем - левый), df_brands (вызываемый)
print(pd.merge(df_products, df_brands, on='brand_id'))

# Добавить новые данные, чтобы нарушить целостность данных
df_brands.loc[6] = [7, 'MSI']
df_products.loc[11] = [12, 'Ноутбук Huawei', 8]

# print(pd.merge(df_products, df_brands, on='brand_id', how='inner')) # inner - только если в двух таблицах есть brand_id
# print(pd.merge(df_products, df_brands, on='brand_id', how='left')) # left - все записи из левой, а если в правой нет, то NaN
# print(pd.merge(df_products, df_brands, on='brand_id', how='right')) # right - все записи из правой, а если в левой нет, то NaN
# print(pd.merge(df_products, df_brands, on='brand_id', how='outer')) # все записи из левой и все из правой, и если нет соответствия, то добавить NaN

# Если переименовать столбец ===============================
df_brands.rename(columns={'brand_id':'id'}, inplace=True)
print(df_brands)

print(pd.merge(df_products, df_brands, left_on='brand_id', right_on='id', suffixes=('_left', '_right'), indicator=True, how='outer')) # left_on='brand_id', right_on='id'

# Метод join (соединение на основании ключей - индексов) 
df_brands.set_index('id', inplace=True)
print(df_brands)
 # on - индексы (id) вызывающей таблицы, а не колонки
print(df_products.join(df_brands, on='brand_id', how='inner'))

# HW
# Объедините таблицы городов и стран, добавив к таблице городов наименование страны.
# В итоговом дата фрейме должны быть следующие столбцы:
# • ID (ID города)
# • City (Название города)
# • CountryCode (Код страны)
# • Country (Название страны)
# • * Population (Кол-во населения города) Итоговый датафрейм сохранить в файл Result.xlsx

