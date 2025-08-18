'''WTF'''
n = int(input()) # 3
for i in range(n): # 0 1 2
    for j in range(i+1):
        if j == i:
            print(0, end='')
        elif not j or i == n-1:
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()
