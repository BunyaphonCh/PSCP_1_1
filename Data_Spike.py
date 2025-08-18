'''FIND Max'''
MAX = 0
G = 0
for i in range(8):
    n = int(input())
    if n > MAX:
        MAX = n
    G += i
print(MAX)
