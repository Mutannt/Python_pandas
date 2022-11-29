# 3. Сохранение данных и фильтры в Pandas
import pandas as pd

df = pd.read_csv('2save.csv', sep=",", encoding='cp1251')
print(df)

# Фильтрация данных WHERE Price > 1000
print(df[df["Price"] > 1000])
# Где есть подстрока SELECT .. Like
print(df[df["Product"].str.contains("LG")])
# Инвертировать, всё, что не удовлетворяет условию ~
print(df[ ~df["Product"].str.contains("LG")])
# Два фильтра сразу & - И, | - ИЛИ
print(df[ (df["Product"].str.contains("Batteries")) & (df["Total"] > 10)])


