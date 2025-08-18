'''Tax'''
import math
INCOME = int(input())
TAX = 0
if INCOME > 4_000_000 :
    TAX += math.floor((INCOME-4_000_000) * 0.35)
    INCOME = 4_000_000
if INCOME > 2_000_000 :
    TAX += math.floor((INCOME-2_000_000) * 0.3)
    INCOME = 2_000_000
if INCOME > 1_000_000 :
    TAX += math.floor((INCOME-1_000_000) * 0.25)
    INCOME = 1_000_000
if INCOME > 750_000 :
    TAX += math.floor((INCOME-750_000) * 0.2)
    INCOME = 750_000
if INCOME > 500_000 :
    TAX += math.floor((INCOME-500_000) * 0.15)
    INCOME = 500_000
if INCOME > 300_000 :
    TAX += math.floor((INCOME-300_000) * 0.1)
    INCOME = 300_000
if INCOME > 150_000 :
    TAX += math.floor((INCOME-150_000) * 0.05)
    INCOME = 150_000
print(TAX)
