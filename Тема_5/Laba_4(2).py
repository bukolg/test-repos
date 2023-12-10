# Конвертер из CSV в JSON формат
import csv
import json
res = []
with open('output.csv') as f:
    reader = csv.DictReader(f)
#Создаем для каждой записи словарь в формате JSON, где ключи-названия столбцов, а значения-значения в этой строке
    for row in reader:
        print(row)
        res.append(row)  # Создаем список словарей

print(res)

#Преобразуем список в json-строку
a_list = json.dumps(res, indent = 4)
print(a_list)