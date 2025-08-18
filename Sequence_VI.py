'''Sequence VI'''
n = int(input())
for i in range(n): # 0 1 2 3 4
    for j in range(i+1): # 1 2 3 4 5
        if i == j:
            print(j+1, end='')
        else:
            print(j+1, end=' ')
    print()
