from fractions import Fraction
from datetime import datetime

f1 = Fraction(3, 4)
f2 = Fraction(5, 6)

symma = f1 + f2
vychitanie = f1 - f2
proizvedenie = f1 * f2
delenie = f1 / f2

print(symma)
print(vychitanie)
print(proizvedenie)
print(delenie)

#8
now = datetime.now()

print("Текущая дата и время", now)
print("Текущая дата:", now.date())
print("Текущее время:", now.time())