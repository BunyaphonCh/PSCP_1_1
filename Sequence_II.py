'''II'''
n = int(input()) # 5
for i in range(n): # 0 1 2 3 4
    for j in range(n): # 0 1 2 3 4
        if j == (n-1):
            print(i+(j*n),end='')
        else:
            print(i+(j*n),end=' ')
    print()
