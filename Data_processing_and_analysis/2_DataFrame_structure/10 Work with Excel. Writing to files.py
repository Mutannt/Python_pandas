# Работа с Excel. Запись в файлы
import pandas as pd

# nrows=100 - Вывести только 100 строк
# # df = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\10 city.csv', sep=';', nrows=50)
# df = pd.read_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\10 city.csv', sep=';')
# print(df)

# df['Location'] = df.Name + ', ' + df.CountryCode
# print(df)

# # Excel может не воспринять колонки ID, поэтому её нужно переименовать
# df.rename(columns={'ID':'Number'}, inplace=True)
# print(df)
# df.to_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\10 city2.csv',
# sep=';', index=False)
# # Сохранение выбранных колонок
# df.to_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\10 city3.csv',
# sep=';', index=False, columns=['Number', 'Location', 'Population'])

# Excel Files ====================================================================================================
# sheet_name='1'(второй лист) или sheet_name='names'
# df2 = pd.read_excel(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\10 cities.xlsx',
# engine='openpyxl', sheet_name=0)
# print(df2)

# При чтении можно сделать что-то со значениями ячейки с помощью пользовательской функции. converters=
# Функция разбивки чисел
def Conver_population(val):
    return '{:,}'.format(val) # Форматирование чисел в ython

def Conver_population2(val):
    if val > 100000:
        return '{:,}'.format(val)
    return val

df2 = pd.read_excel(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\10 cities.xlsx',
engine='openpyxl', sheet_name=0, converters={'Population':Conver_population2})
print(df2)

# Запись в excel ====================================================================================================
# Запись с 3 ячейки, три пустых сверху, 1 пустая слева startrow=3, startcol=1
df2.to_excel(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\10 cities2.xlsx',
sheet_name='Format cities', index=False, startrow=3, startcol=1)

# Запись на несколько листов ========================================================================================
df3 = pd.read_excel(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\10 cities.xlsx',
engine='openpyxl', sheet_name='names')
print(df3)
# with ... as - автоматически открывает и закрывает файл
# df3.to_excel()
with pd.ExcelWriter(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\10 cities3.xlsx') as writer:
    df2.to_excel(writer, sheet_name='Format cities', index=False, startrow=3, startcol=1)
    df3.to_excel(writer, sheet_name='Names', index=False)

# Запись двух датафреймов на один и тот же лист
df2 = pd.DataFrame({
    'Страны': ['Франция', 'США', 'Россия', 'Украина'],
    'Столицы': ['Париж', 'Вашингтон', 'Москва', 'Киев'],
    'Численность населения': [66.99, 328.2, 145.5, 41.98]
})
with pd.ExcelWriter(r'D:\Big Data\python\pandas\Data_processing_and_analysis\2_DataFrame_structure\10 cities4.xlsx') as writer:
    df2.to_excel(writer, sheet_name='Тест', index=False)
    df3.to_excel(writer, sheet_name='Тест', index=False, startrow=len(df2)+2) # Отступ 1 строка или df2.shape[0]



