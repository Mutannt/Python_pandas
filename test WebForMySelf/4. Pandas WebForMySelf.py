# Объединение датафреймов в Pandas
import pandas as pd

df = pd.read_csv('2save.csv', encoding='cp1251')

print(df.shape) # Кортеж с размерностьЮ датафрейма

num = 1 # Именование файлов

# Цикл разбиение по файлам с шагом 5000 (в range последний элемент не включается)
for i in range(0, df.shape[0], 5000):
    # print(i)
    # df.loc[0] # Возми всю нулевую строку целиком
    # df.loc[0:5000] # Строки от 0 до 5000
    # print("========================================")
    tmp = df.loc[i:i+5000-1]
    tmp.to_csv(f'4_files/4file_{num}.csv', encoding='cp1251', index=False)
    num+=1

# Объединение файлов
import os # Для работы с файлами

df_all = pd.DataFrame() # Пустой датафрейм

for f in os.listdir("4_files/"):
    # print(f)
    tmp = pd.read_csv("4_files/" + f, encoding='cp1251')
    # UNION (сложение отднотипных таблиц)
    df_all = pd.concat([df_all, tmp])

print(df_all)
# Но при объединение индексы повторяются
# Поэтому можно переиндексировать. inplace - переиндексировать, drop - чтобы не сохранять старые индексы
df_all.reset_index(inplace=True, drop=True)