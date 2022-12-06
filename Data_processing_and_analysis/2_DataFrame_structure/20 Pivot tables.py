# Сводные таблицы
import pandas as pd

# cities = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\2 city.csv', sep=';')
# print(cities)

# # Группировка по стране и среднее значение (mean)
# print(cities.pivot_table(index='CountryCode', values='Population', aggfunc='sum'))

# 2 файл ========================================================================
# df = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\20 ratings.csv')
# print(df)

# # Сколько раз пользователь выставил оценки
# print(df[ df.userId == 1 ].rating.value_counts())
# print(df.groupby('userId')['rating'].value_counts().head(12))

# # Сводные таблицы
# print(df.pivot_table(values='movieId', index='userId', columns='rating', aggfunc='count'))

# # Заменить NaN на 0 (fill_value=0)
# print(df.pivot_table(values='movieId', index='userId', columns='rating', aggfunc='count', fill_value=0))

# # Подведение итогов  margins=True
# print(df.pivot_table(values='movieId', index='userId', columns='rating', aggfunc='count', fill_value=0, margins=True))

# data = df.pivot_table(values='movieId', index='userId', columns='rating', aggfunc='count', fill_value=0, margins=True)

# # Сортировка по столбцу 5.0 по убыванию
# print(data.sort_values(by=5, ascending=False))
# 3 файл ========================================================================

sales = pd.read_excel(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\20 sales-funnel.xlsx', engine='openpyxl', sheet_name=0)
print(sales)

# Группировка по названию и берём среднее значение
print(sales.pivot_table(index='Name'))

# Вложенная группировка
print(sales.pivot_table(index=['Manager', 'Name']))

# Группировка с суммированимем
print(sales.pivot_table(index='Manager', aggfunc='sum'))

# Сводная по менеджеру и компании
print(sales.pivot_table(index='Manager', columns='Name', values='Price', aggfunc='sum', fill_value=0, margins=True))
# Поменять оси
print(sales.pivot_table(index='Name', columns='Manager', values='Price', aggfunc='sum', fill_value=0, margins=True))

# Две колонки
print(sales.pivot_table(index='Name', columns=['Manager', 'Quantity'], values='Price', aggfunc='sum', fill_value=0, margins=True))

# Две агрегирующие функции
print(sales.pivot_table(index='Name', columns='Manager', values='Price', aggfunc=['sum', 'count'], fill_value=0, margins=True))


