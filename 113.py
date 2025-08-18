'''dfefsa'''
num = input()
RESULT = []
PERFECT = ''
for i in num:
    RESULT.append(i)
    if len(RESULT) >= 3 and RESULT[-3:] == ['1','1','3']:
        RESULT.pop()
        RESULT.pop()
        RESULT.pop()
for i in RESULT:
    PERFECT += i
print(PERFECT)
