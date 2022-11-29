# Задание 1-2. Удаление пустых значений
import pandas as pd

# 2. Проанализировать данные и почистить
#   а. Удалить отсутствующие значения (или заменить)
df = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\3 Practicing with Pandas\2 result.csv', sep=',')
print(df)

# Статистика
df.info(memory_usage='deep')

# Удаление пустых значений
df.dropna(how='any', inplace=True)
print(df)

# Статистика
df.info(memory_usage='deep')


df.to_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\3 Practicing with Pandas/3 result.csv', index=False)



