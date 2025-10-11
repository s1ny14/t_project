from decimal import Decimal, getcontext
getcontext().prec = 28 # до 28 десятичных знаков

P = Decimal(input("Введите сумму, которую хотите положить на счет: ").strip()) # нач сумма
r = Decimal(input("Введите процентную ставку: ").strip()) # проц ставка на год
t = Decimal(input("Введите срок хранения денежных средств в годах: ").strip()) # срок в годах

monthly_rate = r / Decimal('100') / Decimal('12') # расчет месячной ставки

mount = Decimal('12') * t # расчет экспоненты

S = P * (Decimal('1') + monthly_rate) ** mount # итоговая сумма

profit = S - P # прибыль

print("Итоговая сумма: ", S.quantize(Decimal('0.01')))
print("Прибыль: ", profit.quantize(Decimal('0.01')))