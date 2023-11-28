#Лаба_1(3)
# Необходимо определить количество игроков в списке и разделить игроков на две равные команды
players = ["Юля", "Ден","Лев", "Оля", "Ник", "Тим", "Аня", "Яна"]
quantity = len(players)
print(f"Общее количество игроков в списке {quantity}")
middle = int(quantity/ 2)
team1 = players[:middle]
team2 = players[middle:]
print(f"Состав первой команды:  {team1}")
print(f"Состав второй команды:  {team2}")