"""Ahhhhh"""
import math
layer = int(input())
sell = int(input())
amount = 0
for i in range(layer):
    i+=1
    amount += (i * i)
left = amount - sell
cal = math.floor(left / sell)
print(cal)