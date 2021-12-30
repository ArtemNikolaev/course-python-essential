# https://github.com/ArtemNikolaev/gb-hw/issues/18

seasons = {
    'ЗИМА': [12, 1, 2],
    'ВЕСНА': [3, 4, 5],
    'ЛЕТО': [6, 7, 8],
    'ОСЕНЬ': [9, 10, 11]
}

month = int(input('Введите номер месяца: '))

if month < 1 or month > 12:
    print('Месяцев всего 12. Поэтому минимальное значение - 1, а максимальное - 12')
else:
    for season in seasons:
        if month in seasons[season]:
            print('Сезон выбранного тобой месяца: ' + season)
            break
