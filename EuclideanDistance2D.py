"""Find distance by using euclidean between"""
import math
q1 = float(input())
q2 = float(input())
p1 = float(input())
p2 = float(input())
compute = math.sqrt(((q1-p1) ** 2) + ((q2-p2) ** 2))
print(compute)
