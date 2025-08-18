'''Ball'''
n = float(input())
COUNT = 0
while True:
    n *= (3/5)
    if n < 0.01:
        break
    COUNT += 1
print(COUNT)
