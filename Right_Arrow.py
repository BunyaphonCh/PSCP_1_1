'''Right Arrow'''
k = int(input())
n = int(input())
LENGTH = (n-1)//2
for i in range(LENGTH):
    print((i*' ')+(k*'*'))
LENGTH2 = n - LENGTH
for i in range(LENGTH2):
    print((((LENGTH2-1)-i)*' ')+(k*'*'))
