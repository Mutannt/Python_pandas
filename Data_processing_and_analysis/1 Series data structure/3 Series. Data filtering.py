# Фильтрация данных Series
import pandas as pd

cities = pd.Series(
    {'Челябинск': 1179288, 'Екатеринбург': 1544376, 'Париж': 2000000, 'Берлин': 3800000},
     index=['Челябинск', 'Париж', 'Берлин', 'Милан']
     )
# Нет Екатеринбурга, т.к  в index он не прописан
print(cities)

# print(cities.isnull()) # Поиск нулевых значений (True/False)
# print(cities.notnull()) # Поиск ненулевых значений  (True/False)

# print(cities > 1000000) # (True/False)

# print(cities['Челябинск'])

# Все записи с True
print(cities [cities.isnull() ])
print(cities [cities.notnull() ])
print(cities [cities > 1000000 ])

# Комбинирование фильтров
# Города с населением >1 500 000, но меньше 3 000 000
print(cities [(cities > 1500000) & (cities < 3000000)])

# Города с населением больше 1 000 000 и население не равно 2 000 000
print(cities [(cities > 1000000) & (cities != 2000000)])

# ~ Инвертировать результат ~(Условие) тильда перед условием !

for index, value  in cities.items():
    print(f'Index: {index}, Value: {value}')








