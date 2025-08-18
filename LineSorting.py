'''LineSorting'''
n = int(input())
ALL = []
for i in range(n):
    text = input()
    ALL.append(text)
ALL.sort(key=len)
for i in ALL:
    print(i)
