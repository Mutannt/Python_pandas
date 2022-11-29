# Метод apply
import pandas as pd

# Метод apply применяет функцию/lambda-выражение для каждого значения серии или каждого из значения строки (как в цикле)
# Можно применять как к столбцу df['Population'].apply(...)
# так и в целом к датафрейму df_country.apply(get_density, axis=1)

df = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\10 city.csv', sep=';')
print(df)
# Создать столбец
df['cnt'] = 5
print(df)

# Если cnt > 100, то 
df.cnt = df['cnt'].apply(lambda x: 1 if x > 100 else 2)
print(df)
# Удаление столбца
df.drop(columns='cnt', inplace=True)
print(df)

# 2 Столбец с длиной строки
df['len_Name'] = df['Name'].apply(len)
print(df)

# Население города > 10 000 000 - Megacity Если > 1 000 000 - large
def get_size(param):
    if param > 10000000:
        return 'Megacity'
    elif param > 10000000:
        return 'Large'
    elif param > 500000:
        return 'Medium'
    else:
        return 'Small'

df['size'] = df['Population'].apply(get_size)
print(df)

# Группировка и подсчёт количества
print(df['size'].value_counts())
print(df [df['size'] == 'Megacity'])

# Лямбда функция
df['size2'] = df['Population'].apply(
    lambda param: 'Megacity' if param > 10000000
    else 'Large' if param > 10000000
    else 'Medium' if param > 500000
    else 'Small')
print(df)

df_country = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\13 country.csv', sep=';')
print(df_country)

# Плотность - Density
def get_density(row):
    return int(row['Population'] / row['SurfaceArea'])
# При применении к дата фрейму доступна любая колонка axis=1(колонки)
df_country['Density'] = df_country.apply(get_density, axis=1)
print(df_country)

# В pandas скорее всего вы сможете обойтись без циклов, только в крайних случаях желательно использовать.
# # Ципкл по столбцу
# for index, value  in cities.items():
#     print(f'Index: {index}, Value: {value}')

#  Как пройтись в цикле по датафрейму
for index, row  in df_country.iterrows():
    print(index, row.Name, row.Density, sep=' | ')

# Страны с нулевой плотностью
print(df_country[df_country.Density == 0])