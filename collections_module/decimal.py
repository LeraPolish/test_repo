"""
Щоб контролювати точність обчислень
"""
from decimal import Decimal

print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))
print(Decimal("0.1") + Decimal("0.2"))
"""
Точність обчислень з Decimal контролюється через контекст. 
Можна налаштувати загальну точність для всіх обчислень Decimal.
"""
from decimal import Decimal, getcontext

getcontext().prec = 6
print(Decimal("1") / Decimal("7"))

getcontext().prec = 8
print(Decimal("1") / Decimal("7"))
