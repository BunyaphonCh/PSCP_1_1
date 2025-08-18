'''IV'''
m = int(input())
X = 1
for _ in range(m):
    _ = _ * 1
    for j in range(1,m+1):
        if j == m:
            print(X,end='')
        else:
            print(X,end=' ')
        X+=1
    print()
