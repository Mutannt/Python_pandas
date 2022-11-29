# Тип данных Category
import pandas as pd
# Тип object занимает довольно много места, а тип category меньше
# Тип enum 1=>RU, 2=>EN (видим как RU, но хранит 1,2)
# В категорию лучше помещать данные, которые повторяются и которых много. И столбец будет редко изменяться
# На каждый не надо, может навредить!

df = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\2 city.csv', sep=';')
print(df)

# Сколько уникальных значений
# print(df.District.nunique())
# print(df.CountryCode.nunique())

# Важно, если файл весит много от 1 ГБ
# Сколько памяти занимает memory usage
df.info() # 159.5+ KB   = Примерное значение
df.info(memory_usage='deep') # Реальный расход памяти 846.9 KB
# По клонкам расход памяти
print(df.memory_usage()) # Приближенное значение
print(df.memory_usage(deep=True))#.sum()) # Реальный расход памяти

# Тип category
df['CountryCode'] = df.CountryCode.astype('category')
df.info(memory_usage='deep') # Теперь занимает 639.4 KB
print(df.memory_usage(deep=True))

# в jupiter-e, (скорость выполнения)
# %%timeit
# print(df.groupby('CountryCode').count())


# 2 Метод cat есть только у той серии для которой назначена category
# .cat.codes pandas представляет категории как цифры (индексы) по алфавиту. Как содержание в книге
print(df.CountryCode.cat.codes)

# =================================================================
df2 = pd.DataFrame({
    'name': ['John', 'Jack', 'Katy', 'Paul', 'Susan'],
    'mark': ['good', 'excelent', 'bad', 'middle', 'good']
})
print(df2)

# Выбрать только с оценками 'good' и 'excelent'
# 2.1 Способ
def get_mark(v):
    if v == 'good':
        return 4
    elif v == 'excelent':
        return 5
    elif v == 'bad':
        return 2
    else:
        return 3

df2['rate'] = df2.mark.apply(get_mark)
print(df2[ df2.rate > 3 ])

# 2.2 Способ  .map() - замена значений
d_mark = {'good': 4, 'excelent': 5, 'bad': 2, 'middle': 3}

df2['rate2'] = df2.mark.map(d_mark)
print(df2[ df2.rate > 3 ])

# 2.3 с помощью category + сортировка по category
# Сразу надо отсрортировать ordered=True(уже отсортированы), само бы отсортировалось по алфавиту, что неправильно 
df2['mark'] = pd.Categorical(df2.mark, categories=['bad', 'middle','good', 'excelent'], ordered=True)
df2.info() # Уже категория
print(df2.mark) # Есть знак меньше Categories (4, object): ['bad' < 'middle' < 'good' < 'excelent']
print(df2[ df2.mark > 'middle'])
print(df2[ df2.mark > 'middle'].sort_values(by='mark', ascending=False)) # по убыванию

# print(df2.mark.max()) # excelent