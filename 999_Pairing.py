"""Find password"""
length = int(input())
first = input()
second = input()
COUNT = 0
for i in range(length):
    if int(first[i]) + int(second[i]) == 9:
        COUNT += 1
if COUNT == length:
    print('YES')
else:
    print(f'NO {length - COUNT}')
