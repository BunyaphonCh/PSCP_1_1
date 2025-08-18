"""Pongg"""
num = int(input())
STRR = str(num)
if not num % 3 or STRR[-1:] == '3':
    print('PONG')
else:
    print(num)
