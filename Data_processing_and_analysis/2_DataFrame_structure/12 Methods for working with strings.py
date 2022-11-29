# Методы для работы со строками
import pandas as pd

df = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\10 city.csv', sep=';')
print(df)

# 1 Найти города, которые начинаются на 'Ка' и с нижненго регистра, и с верхнего
# Если хочешь использовать регулярные выражения, то надо параметр regex=True (по умолчанию True)
# pat= - Шаблон по которому производится поиск
# case=False (Без учёта регистра) или flags=re.IGNORECASE
# na=False - Исключить NaN из выборки

# print(df['Name'].str.contains('ka', case=False)) # True Где содержится 'ka'
print(df[ df['Name'].str.contains('^ka', case=False) ]) # Строки где содержится 'ka'

# 2 Города ничанающиеся на 'kа', но состоящие из одного слова (Букву ё отдельно)
print(df[ df['Name'].str.contains('^ka[a-zš]+$', case=False) ])
# Для игнорирования регистра также можно использовадь модуль re
import re
print(df[ df['Name'].str.contains('^ka[a-zš]+$', flags=re.IGNORECASE) ])

# 3 Города, которые начинаются на 3 буквы 'kab' или 'kar'
print(df[ df['Name'].str.contains('^(kab|kar)[a-zš]+$', case=False) ])

# =====================
# Увеличить длину колонки
pd.set_option('max_colwidth', 80)

df2 = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\9 price.csv', sep=';')
print(df2)

# 4 Выбрать строки с названием 'Ноут'. Регулярные нельзя применять к пустым NaN строкам
# df2.dropna(subset=['title'], inplace=True)
# print(df2)
print(df2[ df2['title'].str.contains('^Ноут ', case=False, na=False) ]) # Нет NaN


# str. lover, upper, title (каждое слово с большой буквы),
# capitilize (Первую букву в предложении большой)
# swapcxase (большую маленькой, маленькую большой),
# casefold Исправляет предложения. 'Вернет реГистр СвеРнутоЙ копии Cтроки' в 'вернет регистр свернутой копии cтроки'
# df2.title = df2['title'].str.lower()
# df2.title = df2['title'].str.upper()
# df2.title = df2['title'].str.capitalize()
# df2.title = df2['title'].str.title()
# df2.title = df2['title'].str.swapcase()
# df2.title = df2['title'].str.capitalize()
# df2.title = df2['title'].str.casefold()
print(df2)

# Сколько раз встречается буква 'н' в словах
print(df2.title.str.count('н', flags=re.IGNORECASE)) # Без учёта регистра

# Только те записи, где 'н' встречается более одного раза
print(df2 [df2.title.str.count('н', flags=re.IGNORECASE) > 1] )

# Записи со скидной 'суперцена'
print(df2[ df2['title'].str.contains('Суперцена', case=False, na=False) ]) # Нет NaN
# print(df2 [df2.title.str.count('Суперцена', flags=re.IGNORECASE) == 1])
# print(df2[ df2['title'].str.endswith('Суперцена', na=False) ]) # Нет NaN, Endswith совпадение с концом строки

# Замена строк replace
print(df2['title'].str.replace(' ', '_'))
# Замена пробелов в шапке таблицы и приведение к нижнему регистру
df2.columns = df2.columns.str.replace(' ', '_').str.lower()
print(df2)