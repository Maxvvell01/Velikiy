money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months_ = 0
budget = money_capital + salary - spend
exp = spend + spend * increase

while exp < budget:
    budget = budget + salary - exp - exp * increase
    months_ += 1

print("Количество месяцев, которое можно протянуть без долгов:", months_)
