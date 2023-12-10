# Реализовать функцию, которая прочитает JSON файл и найдет сумму произведений двух значений в каждом словаре.
# Значения для умножения находятся по ключам "score" и "weight"
import json
def sumproduct(data_):
    with open(data_) as f:
        data = json.load(f)
    print(f"JSON файл {data}")

    score = []
    weight= []
    for i in data:
        score.append(i['score'])
        weight.append(i['weight'])

    print(f"Значения по ключу score {score}")
    print(f"Значения по ключу weight {weight}")

    summ_pr = 0
    for i in range(len(score)):
        summ_pr += score[i]*weight[i]
        summ_pr = round(summ_pr, 3)
    print(f"Сумма произведений={summ_pr}")
    return summ_pr

print(sumproduct('sw_data.json'))









