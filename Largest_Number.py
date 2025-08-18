"""Ahhhh"""
a = int(input())
b = int(input())
c = int(input())
numbers = [a, b, c]
RESULT = ""
if a >= b and a >= c:
    if b >= c:
        RESULT = a + b + c
    else:
        RESULT = a + c + b
elif b >= a and b >= c:
    if a >= c:
        RESULT = b + a + c
    else:
        RESULT = b + c + a
else:
    if a >= b:
        RESULT = c + a + b
    else:
        RESULT = c + b + a
print(RESULT)
