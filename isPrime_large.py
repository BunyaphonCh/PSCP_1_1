'''Is Prime'''
n = int(input())
IS_PRIME = 'YES'
if n == 1:
    print('NO')
elif n == 2:
    print('YES')
elif not n % 2:
    print('NO')
else:
    for i in range(3,int(n**0.5),2):
        if not n % i:
            IS_PRIME = 'NO'
    print(IS_PRIME)
