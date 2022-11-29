# Работа с NaN (пусто)
import pandas as pd

df = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\9 price.csv',
sep=';')
print(df)

print(df.isna())
print(df.isna().sum()) # Суммирует True в столбцах

df.info()

# Строки с Пустой Ценой (price)
print(df[ df.price.isna() ])
# Строки с NaN qty, но столбцы с id по price
print(df.loc[ df.qty.isnull(), 'id':'price' ])

# Обработка удаление строк
print(df)
# Удалить все строки где есть NaN (how='any')
print(df.dropna())
# Только те строки, где все колонки NaN
print(df.dropna(how='all'))
# Удалить только те, где и price и qty = NaN
print(df.dropna(how='all', subset=['price', 'qty']))

# Заполнение отсутствующих значений чем-то другим из других строк
print(df.fillna(value=0)) # Замена всех NaN на 0
print(df.fillna(value={'id':'-', 'title':'-', 'price':0, 'qty':0}))
print(df)
# backfill - bfill, pad- ffill (Значение берётся из уже существующей строки в datafreme)
print(df.fillna(method='ffill')) # Из строки перед
print(df.fillna(method='bfill')) # Из строки после

print(df)
print(df.qty.value_counts(dropna=False)) # Количество вхождений NaN


