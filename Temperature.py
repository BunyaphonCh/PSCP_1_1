"""ajfeofjae"""
temp = float(input())
unit = input()
unit_want = input()
RESULT = 0
CELSIUS = 0
if unit == unit_want:
    RESULT = temp
else:
    if unit_want == 'C':
        if unit == 'F':
            RESULT = f'{((temp-32)*5)/9:.2f}'
        elif unit == 'K':
            RESULT = f'{temp-273.15:.2f}'
        elif unit == 'R':
            RESULT = f'{((temp*5)/9)-273.15:.2f}'
    if unit_want == 'K':
        if unit == 'F':
            CELSIUS = ((temp-32)*5)/9
        elif unit == 'C':
            CELSIUS = temp
        elif unit == 'R':
            CELSIUS = ((temp*5)/9)-273.15
        RESULT = f'{CELSIUS+273.15:.2f}'
    if unit_want == 'F':
        if unit == 'C':
            CELSIUS = temp
        elif unit == 'K':
            CELSIUS = temp - 273.15
        elif unit == 'R':
            CELSIUS = ((temp*5)/9) - 273.15
        RESULT = f'{((CELSIUS * 9) / 5)+32:.2f}'
    if unit_want == 'R':
        if unit == 'F':
            CELSIUS = ((temp-32)*5)/9
        elif unit == 'K':
            CELSIUS = temp - 273.15
        elif unit == 'C':
            CELSIUS = temp
        RESULT = f'{((CELSIUS + 273.15)*9)/5:.2f}'
print(RESULT)
