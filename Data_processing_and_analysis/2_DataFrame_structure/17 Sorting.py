# Сортировка
import pandas as pd

df = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\10 city.csv', sep=';')
print(df)

# sort_values
# ascending=True (по возр), False (По убыв),
# na position (пустые строки) First, last в начале, в конце
# ignore index True - Переиндексировать 0,1,2... или .reset_index()

# print(df.sort_values('Population'))
print(df.sort_values(by='Population', ascending=False, ignore_index=True))
print(df.sort_values(by='Population', ascending=False).reset_index(drop=True)) # drop=True - удалить индексы

# Множественная сортировка
# Сортировка по стране и потом по городу
print(df.sort_values(by=['CountryCode', 'Name'], ascending=True).head(50)) # drop=True - удалить индексы

# Взять первые 10 записей по возрастанию (Выбрать макс насел в стране)
# print(df.groupby('CountryCode')[['Population']].max().sort_values('Population', ascending=False))
print(df.groupby('CountryCode')['Population'].sum().to_frame().sort_values('Population', ascending=False).head(10))

# df2 = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\13 country.csv', sep=';')
# print(df2)

# Сначлаа строки с NaN
# print(df2.sort_values(by='GNPOld', ascending=False, na_position='first'))


