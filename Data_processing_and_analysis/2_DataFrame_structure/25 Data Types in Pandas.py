# Типы данных в Pandas
import pandas as pd

df = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\25 price.csv', sep=';')
print(df)

# Первичная инфа, статистика NaN (object - строка)
df.info()
# Получить типы данных столбцов
print(df.dtypes)

# Замена доллара. Можно использовать регулярные выражения для замены и доллара и рубля
# print(df.price.str.replace('$', ''))
print(df.price.str.replace('\$|₽', '')) # Регулярные варажения
df['price'] = df.price.str.replace('\$|₽', '') # Регулярные варажения

# Приведение к типу. astype(dtype='int32') ===============
# print(df.price.astype('int')) # int32
# print(df.price.astype('int8')) # int8
# print(df.price.astype('uint8')) # uint8 (0...255)
# print(df.price.astype('float')) # float64 с двойной точностью, float32 (если не нужна высокая точность)

df['price'] = df.price.astype('int8')
print(df.dtypes)
# или
# print(pd.to_numeric(df.price, downcast='integer')) # float64, int64 без downcast
# Добавление тестовых данных
df.loc[11] = [12, 'test', 255]
df['price'] = df.price.astype('uint8')
print(df)

import numpy as np
# Какое макс. и мин. число может хранить тип
print(np.iinfo(df.price))


