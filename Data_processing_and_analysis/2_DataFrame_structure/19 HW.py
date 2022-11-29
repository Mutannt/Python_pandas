# Объединение датафреймов. Метод concat
import pandas as pd

# 1. Считать все листы из книги prices.xlsx
df_acer = pd.read_excel(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\18 prices.xlsx',
engine='openpyxl', sheet_name='Acer')
print(df_acer)

df_asus = pd.read_excel(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\18 prices.xlsx',
engine='openpyxl', sheet_name='Asus')
print(df_asus)

df_hp = pd.read_excel(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\18 prices.xlsx',
engine='openpyxl', sheet_name='HP')
print(df_hp)

# ==========================================================
# Если много листов, то можно считать в цикле
f = pd.ExcelFile(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\18 prices.xlsx',
engine='openpyxl')
# print(f)
res = pd.DataFrame() # Пустой датафрейм
for name_list in f.sheet_names:
    # print(name_list)
    tmp = pd.read_excel(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\18 prices.xlsx',
    engine='openpyxl', sheet_name=name_list)
    res = pd.concat([res, tmp], ignore_index=True)
print(res)
# ==========================================================

# 2. Объединить прочитанные дата фреймы в один датафрейм.
df_all = pd.concat([df_asus, df_acer, df_hp], ignore_index=True)
print(df_all)

# 3. Отсортировать по цене в порядке убывания цены.
df_all.sort_values(by='price', ascending=False, inplace=True)
# 4. Сохранить итоговый датафрейм в файл all_prices.xlsx с названием листа Notebooks.
df_all.to_excel(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\19 all_prices.xlsx',
sheet_name='Notebooks', index=False)