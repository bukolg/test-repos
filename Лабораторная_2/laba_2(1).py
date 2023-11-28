money_capital = int(input('Задайте подушку безопасности в рублях: '))
salary = int(input('Задайте ежемесячную зарплату в рублях: '))
spend = int(input('Задайте ежемесячные расходы в рублях: '))
print (money_capital, salary, spend)
n = 0
increase = 1.05 # С учетом ежемесячного роста цен
rising_spend = spend # Траты с учетом роста цен
debt = rising_spend -salary # Ежемесячный долг - траты с учетом роста цен за вычетом зарплаты
while debt < money_capital:
    rising_spend = rising_spend * increase # По условию больше похоже на сложный процент
    debt = debt + rising_spend - salary
    n += 1
n1 = n - n//10 * 10 # Определение последней цифры числа
condition_1 = (n == 1) or (n1 == 1)
condition_2 = (1 < n < 5) or (1 < n1 < 5)
if condition_1:
    print(f"Денег хватит на {n} месяц")
elif condition_2:
    print(f"Денег хватит на {n} месяца")
elif n > 4:
    print(f"Денег хватит на {n} месяцев")
# Для заданных условий money_capital = 20000 руб.  salary = 5000 руб. spend = 6000 руб. increase = 5% денег хватит на 8 месяцев