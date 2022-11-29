# Атрибуты и методы Series. Часть 1
import pandas as pd

cities = pd.Series(
    {'Челябинск': 1179288, 'Екатеринбург': 1544376, 'Париж': 2000000, 'Берлин': 3800000},
     index=['Челябинск', 'Париж', 'Берлин', 'Милан']
     )
# Нет Екатеринбурга, т.к  в index он не прописан
print(cities)

print(len(cities)) # Общий размер
print(cities.shape) # Вернёт количество элементов
print(cities.size) # Общий размер
print(cities.count()) # Количесвто элеентов со значениями. Всё кроме NaN

# Копирование элемента.
# Копирует ссылку, а не серию. Если что-то поменяем, изменится в двух переменных
cities2 = cities
cities2.at["Милан"] = 3200000
print(cities) # Поменялось и в cities

# Глубокое копирование (получить отдельный объект) - deep=True, deep=False поверхностное копирование
cities3 = cities.copy()
print(cities3)
cities2.at['Лондон'] = 9000000
print(cities) # Добавилось и в cities
print(cities3) # Не добавилось в копию

# Вывод по индексу
ds1 = pd.Series([1, 2, 3])
print(ds1)
print(ds1.iat[2]) # 3
# Аналог для Серий
print(ds1.iloc[2]) # 3
print(cities3.loc['Берлин']) # Выведет численность жителей Берлина

#  Агрегация данных (мин, макс, сумм, сред)=====================================================]
# print(cities.min())
# print(cities.max())
# print(cities.sum())
# print(cities.mean())

print(cities.agg('min'))
print(cities.agg('max'))
print(cities.agg('sum'))
print(cities.agg('mean'))
# Лучше использовать agg, т.к можно передавать несколько функций сразу
print(cities.agg(['min', 'max', 'sum', 'mean']))


