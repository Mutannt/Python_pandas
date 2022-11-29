# Переименование колонок
import pandas as pd

# 1 Вариант
# При использовании names нужно перечислять все колонки, хочешь переименовать или нет (недостаток),
# в правильной последовательности
df = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\2 city.csv',
sep=';', names=['id', 'name', 'cc', 'district', 'qty'], header=0)
print(df)
# 2 Вариант (указывать все колонки в прав. порядке)
df = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\2 city.csv',
sep=';')
df.columns = ['id', 'name', 'cc', 'district', 'qty']
print(df)
# 3 Вариант
df = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\2 city.csv',
sep=';')
print(df.rename(columns={
    "ID":"ID города",
    "Name": "Город",
    "CountryCode":"cc"
})) # , inplace=True

# Также в rename можно перадвать функции str.lower Переводит индексы в нижний регистр
df = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\2 city.csv',
sep=';')
print(df.rename(str.lower, axis=1)) # , inplace=True