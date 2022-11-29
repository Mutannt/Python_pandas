# Series. Constructor
import pandas as pd

print(pd.__version__) # Актуальнеая версия

ds1 = pd.Series([1, 2, 3, 4])
print(ds1)
# print(type(ds1)) # pandas.Series

# Значения серии
print(ds1.values)
# print(type(ds1.values)) # numpy.Array

# Индексы серии
# print(ds1.index) # В виде генератора RangeIndex(start=0, stop=4, step=1) [0,4)

ds2 = pd.Series([1, 2, 3, 4], index=["a", "b", "c", "d"])
print(ds2)
# Из словаря
ds3 = pd.Series({"a": 1, "b": 2, "c": 3, "d": 4})
print(ds3)