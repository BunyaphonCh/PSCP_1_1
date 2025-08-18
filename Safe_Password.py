"""Password correct or not"""
PW = "H 4567"
char = input()
num = input()
if PW[:1] == char and PW[2:] == num:
    RESULT = "safe unlocked"
else:
    if PW[:1] == char:
        RESULT = "safe locked - change digit"
    elif PW[2:] == num:
        RESULT = "safe locked - change char"
    else:
        RESULT = "safe locked"
print(RESULT)
