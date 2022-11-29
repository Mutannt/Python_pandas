# Определяем лучшие дни продаж
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

df2 = df.groupby(df.Day_name).agg(['count', 'sum'])['Total']
print(df2)

# Самые пиковые часы продаж по количеству и сумме
# print(df2.sort_values('count', ascending=False).head(5))
# print(df2.sort_values('sum', ascending=False).head(5))

# 1 sum
fig = plt.figure(figsize=(7,5))
ax = fig.add_subplot() # Создаём координатные оси
ax.plot(df2.index, df2['count'], marker="*")
# print(df2.max()[1])
ax.set_title('Сумма продаж по дням недели')
ax.set_xlabel('Дни недели')
ax.set_ylabel('Выручка в $ (mln.)')
# Убрать научный формат
plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)

# Добавление меток
for index, value in enumerate(df2['count']):
    # print(index, value)
    ax.text(index, value + 30, '{0:,}'.format(round(value)).replace(',', ' '), rotation=0,
    color='black', size=12) # По горизонтали, ha - по центру подписи, ha='center'

ax.grid()
plt.show()


# 2 count
fig = plt.figure(figsize=(7,5))
# ИЛИ так
# plt.rcParams['figure.gigsize'] = [12, 8]
ax = fig.add_subplot() # Создаём координатные оси
ax.bar(df2.index, df2['count'])
ax.set_xticks(df2.index)
# print(df2.max()[1])
ax.set_yticks(range(0, int(round(df2['count'].max())), 5000)) # От 0 до 5 млн. с шагом 500 тыс.
ax.set_title('Кол-во продаж по дням недели')
ax.set_xlabel('Дни недели')
ax.set_ylabel('Выручка в $ (mln.)')
# Убрать научный формат
plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)


# Добавление меток
for index, value in enumerate(df2['count']):
    # print(index, value)
    # ax.text(index+1, value, round(value)) # Чуть выше столбика
    ax.text(index, 10000, '{0:,}'.format(round(value)).replace(',', ' '), rotation=90,
    color='white', size=18) # По горизонтали, ha - по центру подписи, ha='center'

ax.grid()
# Сохранить изображение dpi=100 - разрешение изображения
# plt.savefig(r'D:\Big Data\python\pandas\Data_processing_and_analysis\3 Practicing with Pandas/9_img.jpg', dpi=100)
plt.show()

