# Объединение файлов данных
import pandas as pd


df2019 = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\3 Practicing with Pandas\11 names\yob2019.txt',
names=['Name', 'Sex', 'Cnt'])
print(df2019)

# # 1 Самые часто встречающиеся имена
# print(df2019.sort_values('Cnt', ascending=False).head(10))
# # Самые часто встречающиеся имена у девочек за 2019 год
# print(df2019 [ df2019.Sex  == 'F'].sort_values('Cnt', ascending=False).head(10))
# # У мальчиков  за 2019 год
# print(df2019 [ df2019.Sex  == 'M'].sort_values('Cnt', ascending=False).head(10))

# 2 Одно мужское и одно женское имя в один запрос
# Первое в отсортированное попадает, а другие нет
print(df2019.sort_values('Cnt', ascending=False).drop_duplicates('Sex'))

# ==========================================================================
# 3 Объединение в один файл
result = pd.DataFrame() # Пустой датафрейм
print('О май гад')
# с 1880 по 2019
for year in range(1880, 2020):
    tmp = pd.read_csv(f'D:\Big Data\python\pandas\Data_processing_and_analysis\3 Practicing with Pandas\11 names\yob{year}.txt',
    names=['Name', 'Sex', 'Cnt'])
    tmp['year'] = year
    result = pd.concat([result, tmp])

print(result)