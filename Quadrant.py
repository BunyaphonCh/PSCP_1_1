"""What quadrant ?"""
x = int(input())
y = int(input())
Q = 'O'
if not x and not y:
    Q = 'O'
elif x and not y:
    Q = 'X'
elif not x and y :
    Q = 'Y'
elif x > 0 and y > 0:
    Q = 'Q1'
elif x < 0 < y:
    Q = 'Q2'
elif x < 0 and y < 0:
    Q = 'Q3'
elif y < 0 < x:
    Q = 'Q4'
print(Q)
