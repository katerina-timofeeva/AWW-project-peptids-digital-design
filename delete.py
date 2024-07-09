import pandas as pd
import chardet
import re

# Определение кодировки файла
filename = 'POSEIDON.csv'
with open(filename, 'rb') as f:
    result = chardet.detect(f.read())

encoding = result['encoding']
print(f"Detected encoding: {encoding}")

# Загрузка CSV файла с определенной кодировкой и пропуском ошибочных строк
data = pd.read_csv(filename, encoding=encoding, on_bad_lines='skip')  

# Фильтрация строк, где в столбце Units есть символ '%'
filtered_data = data[data['Units'].str.contains('%', na=False)].copy()

# Удаление части строки после символа ± в столбце Uptake
filtered_data['Uptake'] = filtered_data['Uptake'].apply(lambda x: re.split('±', str(x))[0] if '±' in str(x) else x)

# Преобразование значений в столбце Uptake в числовой тип
filtered_data['Uptake'] = pd.to_numeric(filtered_data['Uptake'], errors='coerce')

# Создание нового столбца all_labels и установка значений по умолчанию
filtered_data['all_labels'] = 0

# Установка значений 1 для строк, где Uptake больше или равно 5
filtered_data.loc[filtered_data['Uptake'] >= 5, 'all_labels'] = 1

# Сохранение отфильтрованных данных с добавленным столбцом в новый CSV файл
filtered_data.to_csv('filtered_data_with_labels.csv', index=False)

# Вывод первых нескольких строк новой таблицы для проверки
print("Пример отфильтрованных данных с добавленным столбцом all_labels:")
print(filtered_data.head())

# Вывод пути к сохраненному файлу
print("Отфильтрованные данные с добавленным столбцом all_labels сохранены в файл: filtered_data_with_labels.csv")
