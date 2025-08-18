"""Elo rating system"""
ra = int(input())
rb = int(input())
player = input()
if player == 'A':
    cal = 1 / (1+(10**((rb-ra)/400)))
else:
    cal = 1 / (1+(10**((ra-rb)/400)))
print(f'{cal:.2f}')
