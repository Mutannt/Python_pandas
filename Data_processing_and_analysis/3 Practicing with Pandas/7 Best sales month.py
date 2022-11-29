# Определяем лучший месяц продаж
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter


df = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\3 Practicing with Pandas\6 result.csv', sep=',')
print(df)
df.info()


# Привести к обычному формату (не научный e+06) 
pd.set_option('display.float_format', lambda x: '%.2f' % x)
df2 = df.groupby('Month')[['Total']].sum()
print(df2)

# 1 Вариант графика
# ax = df2.plot(kind='bar', grid=True)
# ax.set_ylabel('$ (mln.)')
# # Убрать научный формат
# ax.get_yaxis().get_major_formatter().set_scientific(False)
# plt.show()

# 2 Вариант графика
fig = plt.figure(figsize=(8,4))
# ИЛИ так
# plt.rcParams['figure.gigsize'] = [12, 8]
ax = fig.add_subplot() # Создаём координатные оси
ax.bar(df2.index, df2.Total)
ax.set_xticks(range(1, 13))
# print(df2.max()[0])
ax.set_yticks(range(0, round(df2.max()[0]), 500000)) # От 0 до 5 млн. с шагом 500 тыс.
ax.set_title('Продажи по месяцам')
ax.set_xlabel('Месяцы')
ax.set_ylabel('Выручка в $ (mln.)')
# Убрать научный формат
plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
# ИЛИ
# sf = ScalarFormatter()
# sf.set_powerlimits((-7, 7)) # Берётся интервал от 10е-4 до 10е4, если превышает, то выносится за скобку
# ax.yaxis.set_major_formatter(sf)

# Добавление меток
for index, value in enumerate(df2.Total):
    # print(index, value)
    # ax.text(index+1, value, round(value)) # Чуть выше столбика
    ax.text(index+1, 300000, '{0:,}'.format(round(value)).replace(',', ' '), rotation='vertical',
    color='white', size=13) # По горизонтали, ha - по центру подписи, ha='center'

ax.grid()
plt.show()



