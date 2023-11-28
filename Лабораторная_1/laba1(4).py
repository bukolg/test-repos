#Лаба_1 (4)
visitings = ['visiting1', 'visiting2', 'visiting3', 'visiting1', 'visiting5', 'visiting4', 'visiting3', 'visiting4', 'visiting2', 'visiting4']

dict_ = dict({"Общее количество": 0, "Уникальные посещения": 0}) #словарь с двумя ключами, начальные значения которых=0

dict_["Общее количество"] = len(visitings) #размер списка с посещениями пользователей
unic_visitings = list(set(visitings)) # количество уникальных посещений
dict_["Уникальные посещения"] = len(unic_visitings) #замена значения в словаре
print("Получившийся словарь статистики", dict_)
