# Атрибуты и методы Series. Часть 2
import pandas as pd

ds = pd.Series([1, 2, 3, 4])
print(ds)

# Если чётно, то сделать нечётное
def test(x):
    if not x % 2: # 0 инвертируется в 1, любое другое число в 0
        return x + 1
    return x

print(ds.apply(test)) # Просто показ результата, сама серия не изменилась
# Поэтому можно перезаписать или применить специальный параметр

# Лямбда фунция
print(ds.apply(lambda x: x + 1 if not x % 2 else x))

# ==========================================================

cities = pd.Series(
    {'Челябинск': 1179288, 'Екатеринбург': 1544376, 'Париж': 2000000, 'Берлин': 3800000})
# Нет Екатеринбурга, т.к  в index он не прописан
print(cities)

cities2 = pd.Series(cities.index)
print(cities2)

# Если в названии города есть буква 'а', то добавить три восклиц знака, иначе вернуть как есть
# Конкатенация. in Есть ли объект в слове
# print(cities2.apply(lambda citi: citi + '!!!' if(citi.find('а') != -1) else citi))
print(cities2.apply(lambda citi: citi + '!!!' if 'а' in citi else citi))
# Если в названии города есть буква 'а', то добавить между буквами знак '-'
# def simbol_a(citi):
#     for simbol in citi:
#         if(simbol == 'а'):
#             return '-'.join(citi)
#     return citi
    
# def simbol_a2(citi):
#     if(citi.find('а') != -1):
#         return '-'.join(citi)
#     return citi

def simbol_a3(citi):
    if('а' in citi):
        return '-'.join(citi)
    return citi

# print(cities2.apply(simbol_a))
# print(cities2.apply(simbol_a2))
print(cities2.apply(simbol_a3))

# Вывести строки где есть буква а
print(cities2[cities2.str.contains('а')])
