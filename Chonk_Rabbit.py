'''Bit Kub'''
num = int(input())
OVER = 0
NAME = ''
MAX = 0
G = 0
for i in range(num):
    name, weight = input().split()
    if int(weight) > 15:
        OVER += 1
    if int(weight) > MAX:
        NAME = name
        MAX = int(weight)
    G += i
print(OVER)
print(f'{NAME} {MAX}')
