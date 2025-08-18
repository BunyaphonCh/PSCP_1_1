'''Reverse'''
RESULT = []
while True:
    text = input()
    if text == 'NULL':
        break
    RESULT.append(text)
for i in RESULT[::-1]:
    print(i)
