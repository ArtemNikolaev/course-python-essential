# https://github.com/ArtemNikolaev/gb-hw/issues/14

revenue = int(input('Введите выручку: '))
costs = int(input('Введите издержки: '))

if revenue < costs:
    print('У вас убытки:', costs - revenue)
else:
    profit = revenue - costs
    print('У вас прибыль:', profit)
    print('Ваша рентабельность:', profit / revenue)

    employees = int(input('Сколько в вашей фирме сотрудников: '))
    print('Прибыль в расчете на одного сотрудника:', profit/employees)

