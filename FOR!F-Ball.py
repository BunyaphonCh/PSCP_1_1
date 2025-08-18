"""Ball"""
text = input()
POS = 1
for i in text:
    if i == 'A':
        if POS == 1:
            POS = 2
        elif POS == 2:
            POS = 1
    elif i == 'B':
        if POS == 2:
            POS = 3
        elif POS == 3:
            POS = 2
    else:
        if POS == 1:
            POS = 3
        elif POS == 3:
            POS = 1
print(POS)
