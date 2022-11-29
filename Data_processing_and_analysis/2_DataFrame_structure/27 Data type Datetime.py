# Тип данных Datetime
import pandas as pd

print(pd.to_datetime('31.10.22')) # 31 месяца не бывает
print(pd.to_datetime('12.11.22')) # уже 12 бывает, поэтому ошибка
print(pd.to_datetime('12.11.22', dayfirst=True)) # 1 Первый идёт день
print(pd.to_datetime('12.11.22', format='%d.%m.%y')) # 2 Вариант

# Возможности типа Datetime
print(pd.to_datetime('12.11.22', format='%d.%m.%y').year) # Получить год

df = pd.DataFrame({
    'date': ['1.01.2008',
             '2.02.2009',
             '3.03.2010',
             '4.04.2011',
             '5.05.2012',
             '6.06.2013',
             '7.07.2014',
             '8.08.2015',
             '9.09.2016',
             '10.10.2017',
             '11.11.2018',
             '12.12.2019',
             '10.11.2022',
             '31.12.2022']
})

print(df)
print(df.dtypes) # Тип object

df['dates'] = pd.to_datetime(df.date, format='%d.%m.%Y')
print(df)
print(df.dtypes) # Тип datetime64[ns]

# dt - класс позволяет использовать методы и атрибуты даты и времени 
print(df.dates.dt.day_name()) # День недели
# dt.year, dt.month, dt.month_name()

# Выборка Все дни больше 10
print(df[ df.dates.dt.day > 10 ])
print(df[ ~(df.dates.dt.day > 10) ]) # <= 10

# Максимальная дата
print(df.dates.max())

# Сколько дней прошло (Вычитание дат)
print(df.dates.max() - df.dates.min()) # 5447 days 00:00:00

# Все даты после 2014-07-07
print(df[ df.dates > pd.to_datetime('2014-07-07' )])

# ======================================================================
# Сколько уникальных записей
print(df.dates.nunique()) # 14

# Если уникальные, то можно назначить колонку в качестве индекса.
# Это даёт удобство при выборке строк
df.set_index(df.dates, inplace=True)
print(df)

# Выбрать все записи за 2022 год
print(df['2022'])
# Год и месяц
print(df['2022-11'])
# Срезы по датам
print(df['2019':'2022'])

# Формат timestamp - кол-во секунд прошедших с 01.01.1970 по текущий день
df2 = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\27 ratings.csv', sep=',')
# print(df2)

df2['dates'] = pd.to_datetime(df2.timestamp, unit='s')
print(df2)