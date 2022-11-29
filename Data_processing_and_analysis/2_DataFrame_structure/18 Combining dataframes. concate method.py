# Объединение датафреймов. Метод concat
import pandas as pd


# Однотипные данные
df_acer = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\18 price_acer.csv', sep=';')
print(df_acer)
df_asus = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\18 price_asus.csv', sep=';')
print(df_asus)
df_hp = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\18 price_hp.csv', sep=';')
print(df_hp)

# Объединить и Переиндексировать
df = pd.concat([df_acer, df_asus, df_hp], ignore_index=True)
print(df)

# Типо многомерный массив
df = pd.concat([df_acer, df_asus, df_hp], keys=['acer', 'asus', 'hp'])
print(df)
# Получить цену из многомерного массива
print(df.loc['asus'].at[1,'price'])

# Редко нужен
# axis = 1 (Объединение столбцов) axis=0 (Добавление строк)
print(pd.concat([df_acer, df_asus, df_hp], keys=['acer', 'asus', 'hp'], axis=1))

# HW
# 1. Считать все листы из книги prices.xlsx
# 2. Объединить прочитанные дата фреймы в один датафрейм.
# 3. Отсортировать по цене в порядке убывания цены.
# 4. Сохранить итоговый датафрейм в файл all_prices.xlsx с названием листа Notebooks.
