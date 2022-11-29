# Конвертирование типов
import pandas as pd


df = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\3 Practicing with Pandas\3 result.csv', sep=',')
print(df)

df.rename(columns={
    'Order ID': 'Order_ID',
    'Quantity Ordered': 'Quantity',
    'Price Each': 'Price',
    'Order Date': 'Order_Date',
    'Purchase Address': 'Address'
}, inplace=True)

# Статистика
df.info()

# Почистить данные от мусора
# Строки с шапками
print(df[ df['Order_ID'].str.contains('Order ID', case=False) ]) # Вывести эти строки
df.drop(df[ df['Order_ID'].str.contains('Order ID', case=False) ].index, inplace=True) # Удалить эти строки


df.Quantity = df.Quantity.astype('int8')
df.Price = df.Price.astype('float')

# Статистика
# df.info()
# df.to_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\3 Practicing with Pandas/4 result.csv', index=False)

# =================================================================================================================================================

# 5 Добавляем колонку Total
# Добавить колонку после колонки цена
df.insert(4, "Total", df.Quantity * df.Price) # 4 - Индекс столбца куда добавить (нач. с 0) 'Total' - название столбца. И значение
print(df)

# ИЛИ
# df2 = df[['Order_ID', 'Product', 'Quantity', 'Price', 'Total', 'Order_Date', 'Address']]
# print(df2)

df.to_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\3 Practicing with Pandas/5 result.csv', index=False)