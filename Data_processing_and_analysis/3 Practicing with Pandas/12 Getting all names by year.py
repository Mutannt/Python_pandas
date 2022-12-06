# Получение всех имен по годам
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\3 Practicing with Pandas\11 result.csv')
# print(df)

# Сравнение количества имён мальчиков с количеством имён девочек. groupby по году и полу
df2 = df.groupby(['Year', 'Sex']).sum()
# df2 = df.groupby(['Year', 'Sex'])['Cnt'].sum() # Если график через df2.plot(kind="bar")
print(df2)

# Работа с мультииндексами
# print(df2.index.get_level_values(0)) # Годы
# print(df2.index.get_level_values(1)) # Пол
# # Выбрать всех девочек
# print(df2.loc[ df2.index.get_level_values(1) == 'F'])
# print(df2.loc[ df2.index.get_level_values(0) == 2019])
# print(df2.loc[ df2.index.get_level_values(0).isin([1880, 2019])]) # 1880 и 2019
#  # С 2010 по 2019
# print(df2.loc[ df2.index.get_level_values(0).isin(range(2010, 2020))])
# print(df2[ df2.index.get_level_values(0).isin(range(2010, 2020))])
# # Всех девочек с 2010 по 2019
# print(df2.loc[ (df2.index.get_level_values(0).isin(range(2010, 2020)))& (df2.index.get_level_values(1) == 'F')])


# unstack - развернуть индекс в колонку
df2 = df2.unstack(level=-1)
print(df2)
# Работа с данными из такой таблицы
# print(df2.loc[2019][0]) # 2019 F
# print(df2.loc[2019].Cnt.F) # 2019 F

# df2.plot(kind="bar")
# df2.plot()
# plt.show()

# # Графики
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot() # Создаём координатные оси
ax.plot(df2.index, df2['Cnt']) # Отображение первого столбца

ax.set_xticks(range(1880, df2.index.max()+1, 5))
# print(df2.max()[1])
# ax.set_yticks(range(0, int(round(df2['count'].max())), 5000)) # От 0 до 5 млн. с шагом 500 тыс.
ax.set_title('Кол-во имён по годам')
ax.set_xlabel('Годы')
ax.set_ylabel('Количество имён')
# Убрать научный формат
plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right') #Наклон подписей по оси x

ax.legend(['Количество женщин', 'Количество мужчин'])
ax.grid()
plt.show()

# ==========================================================================
# Сгруппировать по десятилетиям.
def getDecades(year):
    Hristos = 1800
    while (year >= Hristos):
        Hristos += 10
    return f'{Hristos-10}-{Hristos-10+9}' # Строка

df['Decades'] = df.Year.apply(getDecades)
print(df)

# df3 = df.groupby(['Decades', 'Sex']).sum()['Cnt'] # Если график через df3.plot(kind="bar")
df3 = df.groupby(['Decades', 'Sex']).sum()
df3 = df3.unstack(level=-1)
# График ====================
# 1 Вариант
# print(df3)
# df3.plot(kind="bar")
# plt.show()

# 2 Вариант
fig = plt.figure(figsize=(22,11))
ax = fig.add_subplot() # Создаём координатные оси

x = np.arange(len(df3.index))  # Расположение меток на оси x
width = 0.35  # the width of the bars
ax.bar(x - width/2, df3['Cnt'].F, width, label='Количество женщин')
ax.bar(x + width/2, df3['Cnt'].M, width, label='Количество мужчин')


# ax.set_xticks(x) #range(1880, df2.index.max()+1, 5)
plt.xticks(x, df3.index)
ax.set_title('Кол-во имён по годам')
ax.set_xlabel('Год')
ax.set_ylabel('Количество')
# Убрать научный формат
plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
plt.setp(plt.gca().get_xticklabels(), rotation=90, horizontalalignment='right') #Наклон подписей по оси x


ax.legend()
ax.grid()
plt.show()

# ============================================================
# # # Метод 2: путем построения графика на одной оси
# df = pd.DataFrame({
#     'Name': ['John', 'Sammy', 'Joe'],
#     'Age': [45, 38, 90],
#     'Height(in cm)': [150, 180, 160]
# })
  
# # построение высоты
# ax = df.plot(x="Name", y="Height(in cm)", kind="bar")
# # откладывание возраста на той же оси
# df.plot(x="Name", y="Age", kind="bar", ax=ax, color="maroon")
# plt.show()

# # Метод 1: предоставление нескольких столбцов в параметре y
# df.plot(x="Name", y=["Age", "Height(in cm)"], kind="bar")
# plt.show()