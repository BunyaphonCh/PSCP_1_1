"""Find digit from 7^x"""
num = int(input())
RESULT = 0
if not num % 4:
    RESULT = 1
elif num % 4 == 1:
    RESULT = 7
elif num % 4 == 2:
    RESULT = 9
elif num % 4 == 3:
    RESULT = 3
print(RESULT)
