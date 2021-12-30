# https://github.com/ArtemNikolaev/gb-hw/issues/8

def user(name, surname, year_of_birth, city, email, tel):
    print('Name: ' + str(name) +
          ' | Surname: ' + str(surname) +
          ' | Year: ' + str(year_of_birth) +
          ' | City: ' + str(city) +
          ' | Email: ' + str(email) +
          ' | Tel: ' + str(tel))


user(
    name='Astra',
    surname='Bla',
    year_of_birth=1977,
    city='Baklagan',
    email='mail@email.com',
    tel=32234234134
)