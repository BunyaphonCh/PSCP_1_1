"""Tug warr"""
TEAM_A = 0
TEAM_B = 0
U = 0
for i in range(10):
    n = int(input())
    TEAM_A += n
    U += i
for i in range(10):
    n = int(input())
    TEAM_B += n
    U += i
if TEAM_A > TEAM_B:
    print('B')
elif TEAM_A < TEAM_B:
    print('A')
else:
    print('AB')
