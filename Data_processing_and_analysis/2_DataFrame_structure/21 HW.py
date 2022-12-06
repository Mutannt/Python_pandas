# HW
import pandas as pd


# 1. Прочесть в датафрейм df файл price.csv.
price = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\4 price.csv', sep=';')
price = price[['id', 'title']]
print(price)

# 2.1 Извлечь в колонку brand название бренда из колонки title.
# def brand(row):
#     mas = row.split(' ')
#     return mas[1]

# price['brand'] = price.title.apply(brand)
# print(price)

# 2.2 extract - извлечь данные из строки по маске - рег. выражение
# print(price.title.str.extract('(?P<note>\w+) (?P<brand>\w+)')) # Две серии
# print(price.title.str.extract('\w+ (?P<brand>\w+)'))
price['brand'] = price.title.str.extract('\w+ (?P<brand>\w+)')
print(price)

# 3. Записать уникальные бренды в словарь формата 'brand' :п/п' , где порядковый номер начинается с единицы: {'Acer': 1,
# 'Asus': 2, 'HP': 3, 'Dell': 4, 'Apple': 5, 'Lenovo': (функция enumerate).
brands = price.brand.unique()
print(brands)

# 3.1
# brands = dict(zip(brands, range(1, len(brands)+1)))
# print(brands)
# print(brands['Acer'])
# Использовали функцию zip(), чтобы объединить списки. Эта функция возвращает список кортежей.
# Поскольку нам нужен словарь, для преобразования наших кортежей мы использовали dict().
# 3.2
brands = {}
for el in enumerate(price.brand.unique(), 1):
    # print(el)
    brands[el[1]] = el[0]

print(brands)

# 4.1 Используя полученный словарь, создать колонку brand_id , в которую записать соответствующее значение словаря (на основании
# колонки brand и ключа словаря).
# def get_brad_id(row_brand):
#     for key, value in brands.items(): 
#         if(key == row_brand):
#             return value

# price['brand_id'] = price.brand.apply(get_brad_id)
# 4.2
price['brand_id'] = price.brand.apply(lambda brand: brands[brand])
print(price)

# 5. Создать новый датафрейм df brands из столбцов brand id и brand, удалив при этом дубли (метод drop_duplicates).
# df_brands = price[['brand_id','brand']].drop_duplicates()
df_brands = price.loc[:, ['brand_id','brand']].drop_duplicates()
print(df_brands)

# 6. Удалить из датафрейма df столбец brand.
price.drop(columns='brand', inplace=True)
print(price)

# # 7. Coxранить в файл products.csv датафрейм df (без индексов, разделитель -;).
# price.to_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\21 products.csv', sep=';', index=False)

# # 8. Coxранить в файл brands.csv датафрейм df-brands (без индексов, разделитель -;).
# df_brands.to_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\21 brands.csv', sep=';', index=False)



