# Работа с Excel. Запись в файлы
import pandas as pd

# 1 Считайте файл 10 city.csv
df = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\10 city.csv', sep=';')
print(df)
# 2 Переименовать все колонки в верхний регистр
print(df.rename(str.upper, axis=1, inplace=True))
# 3 Проверить в каких колонках есть отсутствующие значения
df.info()
# 4 Удалить строки с отсутствующими значениями
print(df[ df.DISTRICT.isna() ]) # Строки с отсутствующими значениями
df.dropna(inplace=True)
print(df)
# 5 Выбрать в новый датафрейм строки с населением > 1 000 000
df2 = df[ df.POPULATION > 1000000]
print(df2)
# 6 Удалить столбец District
df.drop('DISTRICT', axis=1, inplace=True)
print(df)
# 7 Записать датафрейм в файл test.xlsx без сохранения индексов
df.to_excel(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\11 test.xlsx', index=False)


