# Библиотека Matplotlib. Часть 1
import pandas as pd
import matplotlib.pyplot as plt

# plot() Если передаешь один параметр, то по оси Y будут значения,
# а по оси X индексы 0, 1, 2, 3
# plt.plot([3, 5, 10, 7, 11])
# plt.show()

# =======================================
# plt.plot([3, 5, 10, 7, 11], range(1, 6))
# plt.show()
# 2 графика сразу ===========================
# plt.plot([3, 5, 10, 7, 11])
# plt.plot([11, 7, 10, 5, 3])
# plt.show()
# ====================================================
df = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\2 city.csv', sep=';')
print(df.head())

# Страны с максимальным количеством населения (10 стран)
print(df.groupby('CountryCode')[['Population']].sum().sort_values(by='Population', ascending=False).head(10))
data = df.groupby('CountryCode')[['Population']].sum().sort_values(by='Population', ascending=False).head(10)

# Столбчатая
# plt.bar(data.index, data.Population)
# plt.show()
# plt.barh(data.index, data.Population) # Горизонтальная
# plt.legend(['Численность населения'])
# plt.title('Топ 10 стран по населению')
# plt.grid()
# plt.show()

# Plot вызов из Pandas (сразу с подписями осей, легендой)====================
# data.plot(kind='barh', grid=True)
# plt.show()

# Круговая
# data.plot(kind='pie', y='Population')
# plt.show()



plt.pie(data.Population, labels=data.index, autopct='%1.1f%%', shadow=True, explode=(0.4, 0.2, 0, 0, 0, 0, 0, 0, 0, 0))
# Разместить легнеду loc='best' (по умолчанию). Сдвиг легенды bbox_to_anchor=(1, .9) - координаты (x,y)
plt.legend(data.index, loc='best', bbox_to_anchor=(1.3, .9))
plt.show()