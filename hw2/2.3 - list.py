# https://github.com/ArtemNikolaev/gb-hw/issues/18

seasons = [
    'ЗИМА',
    'ВЕСНА',
    'ЛЕТО',
    'ОСЕНЬ'
]

month = int(input('Введите номер месяца: '))

if month < 1 or month > 12:
    print('Месяцев всего 12. Поэтому минимальное значение - 1, а максимальное - 12')
else:
    seasonInt = (month % 12) // 3
    print('Сезон выбранного тобой месяца: ' + seasons[seasonInt])