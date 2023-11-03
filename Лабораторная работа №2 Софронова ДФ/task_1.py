money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
total_budget = money_capital
count_month = 0
while True:
    total_budget = total_budget + salary - spend
    spend = spend * (1 + increase)  # Траты на следующий месяц

    if total_budget < 0:
        break

    count_month += 1
print("Количество месяцев, которое можно протянуть без долгов:", count_month)
