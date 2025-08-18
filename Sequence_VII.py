'''Bruh'''
n = int(input()) # 3
for i in range(n): # 0 1 2
    for j in range(i+1): # 0 1 2
        if j == i:
            print(j+1,end='')
        else:
            print(j+1,end=' ')
    print()
for i in range(n-1,0,-1): # 2 1
    for j in range(i): # 1 2 -> 0 | 0 , 1
        if j == i-1:
            print(j+1,end='')
        else:
            print(j+1,end=' ')
    print()
