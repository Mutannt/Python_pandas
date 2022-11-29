# Получение информации о DataFrame
import pandas as pd

df = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\2 city.csv', sep=';')
print(df)
# Вывести сколько-то строк
# print(df.head()) # Показать только начало (первые 4 записи)
# print(df.tail()) # Показать только конец (последние 4 записи)
# print(df.head(10)) # Показать только начало (первые 4 записи)
# print(df.tail(10)) # Показать последние 10 записей
# Максимум 60 строк, иначе переходит к сокращённому стилю

# сведения о датафрейме
print(len(df))
print(df.shape)
print(df.info)
print(df.info()) # Сколько нулевых значений? Сколько памяти занимает

# Найти нулевые значения (пусто - NaN) в district
print(df[ df['District'].isna() ])
# Статистическая информация по колонкам, где числовые значения (count, mean, std, min, max
print(df.describe())

# Первоначальная Группировка
print(df.CountryCode.unique()) # Numpy массив, в котором список уникальных строк
# Сколько уникальных значений
print(len(df.CountryCode.unique()))
print(df.CountryCode.unique().size)

print(df.values) # Numpy массив по строкам из значений

print(df.index) # RangeIndex(start=0, stop=4079, step=1) [0; 4078]

print(df.columns) # Список колонок

# Подсчёт с группировкой и сортировкой (Сколько уникальных значений)
# Код страны и кол-во городов для страны
print(df.CountryCode.value_counts())

print(df.CountryCode.value_counts(normalize=True)) # Сколько каждая группа занимает в процентах

