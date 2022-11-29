# Группировка с фильтрацией
import pandas as pd

df = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\10 city.csv', sep=';')
print(df)

# print(df.groupby('CountryCode')['Population'].sum())

# Как получить датафрейм, а не серию
# print(df.groupby('CountryCode')[['Population']].max()) # Дважды в скобки

# Нормализация индексов
# print(df.groupby('CountryCode')[['Population']].max().reset_index()) # reset_index === as_index=False

# Максимальная численность населения города в стране
# print(df.groupby('CountryCode', as_index=False)[['Population']].max())
#  # Отсортированна по убыванию городов
# print(df.groupby('CountryCode', as_index=False).count().sort_values(by='Population', ascending=False).head(10))

# Фильтр (Страны с количеством городов более 100)
# print(df.groupby('CountryCode', as_index=False).filter(lambda x: len(x['Population']) > 100)) # Записи из групп

# Группы
# 1 SELECT * FROM city GROUP BY CountryCode HAVING count(*) > 100
# Страны с количеством городов более 100 и выбрать город с максимальным количеством жителей в этой стране
print('\n')
print(df.groupby('CountryCode', as_index=False)
.filter(lambda x: len(x['Population']) > 100)
.groupby('CountryCode', as_index=False).max())

# Для доп фильтра Population > 5 000 000
df2 = (df.groupby('CountryCode', as_index=False)
.filter(lambda x: len(x['Population']) > 100)
.groupby('CountryCode', as_index=False).max())

print(df2 [df2.Population > 5000000][['CountryCode', 'Population']])


# 2 С помощью тернарного оператора (Макс. насел. города, но только если размер группы больше 100)
print(
    
    df.groupby('CountryCode').apply(lambda x: x['Population'].max() if len(x['CountryCode']) > 100 else 0)
        .to_frame()
        .sort_values(by=0, ascending=False)
        .rename(columns={0: 'Population'})
        .query('Population > 5000000') # Ещё один метод фильтрации
        .reset_index()
)

# Привести к датафрейму .to_frame()


# Метод для фильтрации данных (Колонки с Population > 8 000 000)
# print(df)
# print(df[ df.Population > 8000000 ])
# print(df.query('Population > 8000000'))







