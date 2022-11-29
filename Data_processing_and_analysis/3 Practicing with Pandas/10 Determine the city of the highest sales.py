#  Определяем город наибольших продаж
import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\3 Practicing with Pandas\6 result.csv', sep=',')
print(df)

# str = '917 1st St, Dallas, TX 75001'.split(',') # Разбивка по запятой
# # .strip() - удаление символов из строки 
# # удаляет начальные и конечные пробелы из строки, если без аргументов
# print(str[1].strip()) 
# str2 = str[2].split(' ')
# print(str2[1])

def get_city(adress):
    city = adress.split(',')[1].strip()
    state = adress.split(',')[2].split(' ')[1]
    return f'{city}, {state}'
    # return city + ' ' + state

df['City'] = df.Address.apply(get_city)
print(df)

# Проверка уникальных значений
print(df.City.unique())

df2 = df.groupby('City').agg(['sum', 'count'])['Total']
print(df2)

fig = plt.figure(figsize=(7,7))
# ИЛИ так
# plt.rcParams['figure.gigsize'] = [12, 8]
ax = fig.add_subplot() # Создаём координатные оси
ax.bar(df2.index, df2['sum'])
ax.set_xticks(df2.index)
# print(df2.max()[1])
ax.set_yticks(range(0, int(round(df2['sum'].max())), 500000))
ax.set_title('Кол-во продаж по городам')
ax.set_xlabel('Города')
ax.set_ylabel('Выручка в $ (mln.)')
# Убрать научный формат
plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right') #Наклон подписей по оси x

# Добавление меток
for index, value in enumerate(df2['sum']):
    # print(index, value)
    # ax.text(index+1, value, round(value)) # Чуть выше столбика
    ax.text(index, 50000, '{0:,}'.format(round(value)).replace(',', ' '), rotation=90,
    color='red', size=13) # По горизонтали, ha - по центру подписи, ha='center'

ax.grid()
# Сохранить изображение dpi=100 - разрешение изображения
plt.savefig(r'D:\Big Data\python\pandas\Data_processing_and_analysis\3 Practicing with Pandas/10_img.jpg', dpi=100)
plt.show()

