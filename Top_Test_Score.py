"""efeweos"""
n = int(input())
MOST = 0
COUNT = 0
U = 0
for i in range(n):
    score = int(input())
    if score > MOST:
        MOST = score
        COUNT = 1
    elif MOST == score:
        COUNT += 1
    U += i
print(MOST)
print(COUNT)
