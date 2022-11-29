import pandas as pd

# Словарь
bank_db = {
    'Name' : ['Иван Иванович', 'Иван Петрович'],
    'Age' : [0, 1],
    'Experience' : [4, 7],
    'Salary' : [75, 95],
    'Credit_score' : [4, 8],
    'Outcome' : [0, 1]
}
 
df = pd.DataFrame(bank_db)
print(df)

# посчитаем средний доход заемщиков (по столбцам): (75 + 95) / 2 mean - среднее значение
print(df['Salary'].mean())
print(df.mean().mean()) # Среднее значение во всех столбцах
print(df.mean(axis=1)) # Среднеее значение для каждой строки
print(pd.concat([df['Name'], df.mean(axis=1)], axis=1)) # Вывести первый столбец с именем и средне значение

