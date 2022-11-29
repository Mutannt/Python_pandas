# DataFrame. Чтение данных
import pandas as pd

# По умолчанию стоит кодировка utf-8, если кириллица использовать cp1251
# Воспринял первую строку как заголовок, поэтому нужно задать заголовки самомст (names)
txt_df = pd.read_csv('2 test.txt', encoding='cp1251', names=['id', 'city', 'population'])
print(txt_df)

cities_df = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\2 city.csv',
sep=';', names=['id', 'city', 'code', 'district', 'population'], header=0) # Переопределить заголовки с помощью names
# heaer=0 - пропустить первую строку
print(cities_df[:3])

df_html = pd.read_html('https://meta.wikimedia.org/wiki/List_of_Wikipedias') 
print(df_html[0])
# Изменить заголовки
df_html[0].columns = ['Номер', 'Язык', 'Язык локальный', 'Вики', 'Статьи', 'Всего страниц',
'Редакторы', 'Администраторы', 'Пользователи', 'Активные пользователи', 'Файлов']
print(df_html[0][:3])
# Вывод из json
df_json = pd.read_json('https://jsonplaceholder.typicode.com/posts')
print(df_json[:3])
