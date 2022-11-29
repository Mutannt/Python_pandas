# Опции и настройки DataFrame
import pandas as pd

# Максимальное кол-во строк, до сокращённого стиля
# print(pd.get_option('max_rows'))
# pd.set_option('max_rows', 100) # 100 до сокращённго стиля
df = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\2 city.csv', sep=';')
# print(df.head(70))

# сколько строк в сокращённом стиле
print(pd.get_option('min_rows'))
pd.set_option('min_rows', 20) # В скоращённом стиле 10 первых и 10 последних
print(df)

# Вернуться к опциям по умолчанию
pd.reset_option('min_rows')
pd.reset_option('all') # Сбросить все опции

df_goods = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\4 price.csv', sep=';')
# Максимальная ширина колонки по умолчанию 50
print(pd.get_option('max_colwidth'))
pd.set_option('max_colwidth', 80)

# Округление двух знаков после запятой, 7.999 ~ 8.00
pd.set_option('precision', 2)

# =============================================================================================
# Максимальное количесвто колонок
print(pd.get_option('max_columns')) # 20
# pd.set_option('max_columns', 30)
print(df_goods)

# Словарь
my_dict = {}
for i in range(1, 31):
    my_dict[f'column {i}'] = [ n for n in range(6) ]

print(my_dict)

test = pd.DataFrame(my_dict)
print(test)
# =============================================================================================

# Генерация тестовых данных
print(pd.get_dummies(list(range(11)), prefix='column'))
