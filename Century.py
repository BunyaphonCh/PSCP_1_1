"""Oejfewpfejwfo"""
import math
n = int(input())
for i in range(n):
    text, year = input().split()
    year = int(year)
    GGR = 0
    GGR += i
    AD_YEAR = 0
    IS_ERROR = False
    if text == 'B.E.':
        AD_YEAR = year-543
        if AD_YEAR <= 0:
            IS_ERROR = True
    elif text == 'A.D.':
        AD_YEAR = year
        if AD_YEAR <= 0:
            IS_ERROR = True
    else:
        IS_ERROR = True
    if IS_ERROR:
        print('ERROR')
    else:
        start_year = math.floor((AD_YEAR + 99) / 100)
        print(start_year)
