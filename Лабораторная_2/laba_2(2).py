salary = int(input('Задайте ежемесячную зарплату в рублях: '))
spend = int(input('Задайте ежемесячные расходы в рублях: '))
increase = int(input('Задайте ежемесячный рост цен в процентах: '))
n = int(input('Задайте количество месяцев: '))
print (salary, spend, increase, n)
n = n + 1
increase = increase / 100 + 1  # С учетом ежемесячного роста цен
rising_spend = spend # Траты с учетом роста цен
debt = rising_spend -salary # Ежемесячный долг - траты с учетом роста цен за вычетом зарплаты
for i in range(2, n): # С учетом расчета 1 месяца до цикла - от 2 до (начального n) +1
    rising_spend = rising_spend * increase # По условию больше похоже на сложный процент
    debt = debt + rising_spend - salary
    debt = round(debt, 2)
print(f"Подушка безопасности на {i} месяцев составит {debt} руб.")
# Для 10 месяцев с условиями salary = 5000 руб. spend = 6000 руб.  increase = 3% Подушка безопасности 18783.26 руб.