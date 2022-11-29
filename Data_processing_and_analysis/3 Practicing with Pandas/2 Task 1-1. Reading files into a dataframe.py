# Чтение файлов в датафрейм
import pandas as pd

# 1. Прочесть содержимое папки '2 files' и собрать всё в единый датафрейм

import os # Для работы с файлами
df_all = pd.DataFrame() # Пустой датафрейм
for f in os.listdir(r"D:\Big Data\python\pandas\Data_processing_and_analysis\3 Practicing with Pandas\2 files/"):
    # print(f)
    tmp = pd.read_csv(r"D:\Big Data\python\pandas\Data_processing_and_analysis\3 Practicing with Pandas\2 files/" + f,
    sep=',', encoding='cp1251')
    # UNION (сложение однотипных таблиц)
    df_all = pd.concat([df_all, tmp])

print(df_all)

df_all.to_csv(r'D:\Big Data\python\pandas\Data_processing_and_analysis\3 Practicing with Pandas/2 result.csv', index=False)












