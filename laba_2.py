money_capital = int(input('Задайте подушку безопасности в рублях: '))
salary = int(input('Задайте ежемесячную зарплату в рублях: '))
spend = int(input('Задайте ежемесячные расходы в рублях: '))
print (money_capital, salary, spend)
n = 0
increase = 1.05 # С учетом ежемесячного роста цен
xx = spend # Траты с учетом роста цен
rr = xx-salary # Ежемесячный долг - траты с учетом роста цен за вычетом зарплаты
while rr < money_capital:
    xx = xx * increase # По условию больше похоже на сложный процент
    rr = rr + xx - salary
    n += 1
n1 = n - n//10 *10
condition_1 = (n == 1) or (n1 == 1)
condition_2 = (n > 1 and n < 5) or (n1 > 1 and n1 < 5)
if condition_1:
    print(f"Денег хватит на {n} месяц")
else:
    if condition_2 :
        print(f"Денег хватит на {n} месяца")
    else:
        if n > 4:
            print (f"Денег хватит на {n} месяцев")