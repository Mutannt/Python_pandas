# Определяем лучшие часы продаж
import pandas as pd
import matplotlib.pyplot as plt
# from matplotlib.ticker import ScalarFormatter


df = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\3 Practicing with Pandas\6 result.csv', sep=',')
print(df)
df.info()

df.Order_Date = pd.to_datetime(df.Order_Date)

df['Hours'] = df.Order_Date.dt.hour
df['Day_name'] = df.Order_Date.dt.day_name()
df.info()
print(df)

df2 = df.groupby(df.Hours).agg(['count', 'sum'])['Total']
print(df2)

# Самые пиковые часы продаж по количеству и сумме
# print(df2.sort_values('count', ascending=False).head(5))
# print(df2.sort_values('sum', ascending=False).head(5))

# # 1 sum
# fig = plt.figure(figsize=(8,4))
# # ИЛИ так
# # plt.rcParams['figure.gigsize'] = [12, 8]
# ax = fig.add_subplot() # Создаём координатные оси
# ax.bar(df2.index, df2['sum'])
# ax.set_xticks(range(0, 24))
# # print(df2.max()[1])
# ax.set_yticks(range(0, int(round(df2.max()[1]))+1600000, 500000)) # От 0 до 5 млн. с шагом 500 тыс.
# ax.set_title('Продажи по часам')
# ax.set_xlabel('Часы')
# ax.set_ylabel('Выручка в $ (mln.)')
# # Убрать научный формат
# plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)


# # Добавление меток
# for index, value in enumerate(df2['sum']):
#     # print(index, value)
#     # ax.text(index+1, value, round(value)) # Чуть выше столбика
#     ax.text(index, value + 200000, '{0:,}'.format(round(value)).replace(',', ' '), rotation=90,
#     color='black', size=11) # По горизонтали, ha - по центру подписи, ha='center'

# ax.grid()
# plt.show()


# 2 count
fig = plt.figure(figsize=(8,4))
# ИЛИ так
# plt.rcParams['figure.gigsize'] = [12, 8]
ax = fig.add_subplot() # Создаём координатные оси
ax.bar(df2.index, df2['count'])
ax.set_xticks(range(0, 24))
# print(df2.max()[1])
ax.set_yticks(range(0, int(round(df2['count'].max()))+9000, 5000)) # От 0 до 5 млн. с шагом 500 тыс.
ax.set_title('Кол-во продаж по часам')
ax.set_xlabel('Часы')
ax.set_ylabel('Выручка в $ (mln.)')
# Убрать научный формат
plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)


# Добавление меток
for index, value in enumerate(df2['count']):
    # print(index, value)
    # ax.text(index+1, value, round(value)) # Чуть выше столбика
    ax.text(index, value + 1000, '{0:,}'.format(round(value)).replace(',', ' '), rotation=90,
    color='black', size=11) # По горизонтали, ha - по центру подписи, ha='center'

ax.grid()
# Сохранить изображение dpi=100 - разрешение изображения
plt.savefig(r'D:\Big Data\python\pandas\Data_processing_and_analysis\3 Practicing with Pandas/8 count_img.jpg', dpi=100)
plt.show()

df.to_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\3 Practicing with Pandas/8 result.csv', index=False)


# ==============================================================================================================

# Используйте base=30вместе с label='right'параметрами в pd.Grouper.
# Указание label='right'делает период времени для начала группировки с 6:30 (более высокая сторона), а не с 5:30.
# Кроме того, по умолчаниюbase установлено значение 0 , поэтому необходимо сместить их на 30, чтобы учесть прямое распространение дат.
# Предположим, вы хотите агрегировать первый элемент каждой подгруппы, тогда:

# df.groupby(pd.Grouper(freq='60Min', base=30, label='right')).first()
# # same thing using resample - df.resample('60Min', base=30, label='right').first()

# ==============================================================================================================

# Timestamp
# df5 = pd.DataFrame(
#     {
#         "Date": [
#             pd.Timestamp("2000-11-02"),
#             pd.Timestamp("2000-01-02"),
#             pd.Timestamp("2000-01-09"),
#             pd.Timestamp("2000-03-11"),
#             pd.Timestamp("2000-01-26"),
#             pd.Timestamp("2000-02-16")
#         ],
#         "ID": [1, 2, 3, 4, 5, 6],
#         "Price": [140, 120, 230, 40, 100, 450]
#     }
# )
  
# # show df
# print(df5)
  
# # Пример 1: Группировка по месяцам
# print(df5.groupby(pd.Grouper(key='Date', axis=0, freq='M')).sum())

# # Пример 2: Группировка по дням
# # freq = ‘5D’, что означает пять дней, поэтому данные группируются с интервалом в 5 дней
# # каждого месяца до последней даты, указанной в столбце даты.
# print(df5.groupby(pd.Grouper(key='Date', axis=0, freq='1D', sort=True)).sum())

# # Пример 3: Группировка по годам
# # Данных группируется по столбцу даты. Поскольку мы указали freq = ‘2Y’,
# # что означает 2 года, поэтому данные группируются с интервалом в 2 года.
# df5.groupby(pd.Grouper(key='Date', freq='2Y')).sum()

# # Пример 4. Группировка по минутам
# # создать массив из 5 дат, начиная с '2015-02-24 00:00:00', по одному в минуту до '2015-02-24 00:09:00'
# dates = pd.date_range('2015-02-24  00:00:00', periods=10, freq='T')
# print(dates)

# df5 = pd.DataFrame({"Date": dates, "ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#                    "Price": [140, 120, 230, 40, 100, 450, 234, 785, 12, 42]})
  
# # данные группируются с интервалом каждые 2 минуты.
# print(df5.groupby(pd.Grouper(key='Date', freq='2min')).sum())