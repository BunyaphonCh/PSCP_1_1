"""Find summ"""
n = int(input())
SUM = 0
for i in range(1,n+1):
    if not i % 3 or not  i % 5:
        SUM += i
print(SUM)
