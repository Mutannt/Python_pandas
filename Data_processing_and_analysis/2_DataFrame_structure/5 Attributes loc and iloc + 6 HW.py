# Атрибуты loc и iloc
import pandas as pd

# Для выборы единичных значений больше подходят at и iat
# loc и iloc призваны выбирать группу рядов и колонок
# .loc[row, column] - выборка по label (индексу)
# .iloc[row, column] - выборка по целочисленному индексу (start, end-1)

df = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\4 price.csv', sep=';')
print(df)

print(df['price'])
print(df[['title', 'price']])

# Строка/колонка
print(df.at[0, 'price'])
# Колонка/Строка
print(df['price'][0])
print(df.loc[0, 'price'])
# Всю строку
print(df.loc[0, :])
# Часть колонок
print(df.loc[0][['id', 'title']])
# Несколько строк
print(df.loc[[0, 1, 3, 4]])
print(df.loc[[0, 1, 3, 4]][['id', 'title']])
# print(df.loc[0:4, ['id', 'title']])
print(df.loc[0:4, :]) # 0-4(5) строки и все столбцы
# Конечная цифра среза в loc включается!
print(df.loc[:, ['id', 'title']]) # Все строки и выбранные столбцы
print(df.loc[:4, 'id':'price']) # Всё от id до price

print(df.iloc[:4, 1:3]) # # 0-3(4) строки в iloc конечная позиция не включается


# ========================================================================================
# 1 Только чётные строки, 2 только нечётные [start:stop:step]  [start, stop)
print(df[0 : : 2]) # Чётные
print(df.loc[0 : : 2]) # Чётные
print(df[1 : : 2]) # Нечётные
print(df.loc[1 : : 2]) # Нечётные
# 3 Перевёрнутый датафрейм
print(df[ : : -1])
print(df.loc[ : : -1])
# 4 Строки с имеющейся ценой
print(df[ ~df.price.isnull() ])
print(df.loc[ df.price.notna(), : ])
# 5 Получить только первую строку
print(df.loc[0, :])
print(df.iloc[0, :])
# 6 Только последнюю строку
print(df.iloc[-1, :])
# 7 Получить только последний столбец
print(df.iloc[:, -1])
print(df.iloc[:, len(df.columns)-1])