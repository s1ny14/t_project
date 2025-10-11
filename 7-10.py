from fractions import Fraction
from datetime import datetime
from datetime import date

#7
f1 = Fraction(3, 4)
f2 = Fraction(5, 6)

symma = f1 + f2
vychitanie = f1 - f2
proizvedenie = f1 * f2
delenie = f1 / f2

print("Сумма: ", symma)
print("Вычитание: ", vychitanie)
print("Произведение: ", proizvedenie)
print("Деление: ", delenie)

#8
now = datetime.now()

print("Текущая дата и время", now)
print("Текущая дата:", now.date())
print("Текущее время:", now.time())

#9
birthday = date(2005, 10, 14) # день рождения
today = date.today() # текущая дата
days_passed = (today - birthday).days # сколько дней прошло с момента рождения

next_birthday_year = today.year # определение следующего дня рождения
if (today.month, today.day) > (birthday.month, birthday.day):
    next_birthday_year += 1
next_birthday = date(next_birthday_year, birthday.month, birthday.day)

days_to_next = (next_birthday - today).days # сколько дней до следующего дня рождения

print("Прошло с рождения: ", days_passed)
print("До следующего дня рождения: ", days_to_next)