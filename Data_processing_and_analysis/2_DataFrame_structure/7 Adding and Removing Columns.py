# Добавление и удаление колонок
import pandas as pd

df = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\4 price.csv', sep=';')
print(df)

# Добавить колонку
df['qty'] = 2
print(df)
# Дублирование колонки
df['test'] = df.id
print(df)

# Вычисляемые колонки
df['total'] = df.price * df.qty
print(df)

cities = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\2 city.csv', sep=';')
print(cities)

cities['Location'] = cities.Name + ', ' + cities.CountryCode
print(cities)

# Удаление колонок, == без перезаписи == axis=0 - по умолчанию (удаление строк), axis=1 - удаление столбцов
print(df.drop(['test'], axis=1))
# ======= inplace=True - перезапись ==========
# df.drop(['test'], axis=1, inplace=True) 
# print(df)
# columns='test' - Удалить массив (список)
# df.drop(columns=['test', 'total'], axis=1, inplace=True) 
# print(df)

# Удаление строк
print(df.drop([1, 5])) # Удалить строки с индексами 1 и 5
# Удалить строки с NaN (пустые)
print(df.price.isna()) # true - строки где NaN
print(df.drop( df.loc[df.price.isna(), :].index) )
print(df.dropna(subset=['price']))

# Заполнить пустые значения нулями 0
print(df.fillna(0))
