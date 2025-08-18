'''Left Arrow'''
k = int(input())
n = int(input())
LENGTH = (n-1)//2
for i in range(LENGTH):
    print((LENGTH-i)*' '+'*'*k)
LENGTH2 = n - ((n-1)//2)
for i in range(LENGTH2):
    print(i*' '+'*'*k)
