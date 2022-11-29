# Добавляем колонку Month
import pandas as pd


df = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\3 Practicing with Pandas\5 result.csv', sep=',')
print(df)

# Order_Date мм.дд.гг привести к типу datetime
df.info(memory_usage='deep') # 48.0 MB
df.Order_Date = pd.to_datetime(df.Order_Date, format='%m/%d/%y %H:%M')
print(df)

df.info(memory_usage='deep') # 36.8 MB datetime64[ns]

df['Month'] = df.Order_Date.dt.month
print(df)

df.to_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\3 Practicing with Pandas/6 result.csv', index=False)



