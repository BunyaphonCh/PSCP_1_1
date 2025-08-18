'''V'''
n = int(input())
COUNT = 0
for i in range(n,0,-1):
    print(i,end='')
    COUNT += 1
    if COUNT == 7:
        print()
        COUNT = 0
    else:
        print(' ',end='')
