'''How many'''
a = int(input())
b = int(input())
if a >= 0 and b >= 0 and not b % 2:
    B = (2*a) - (b/2)
    R = a - B
    if B < 0 or R < 0:
        print('Impossible')
    else:
        print(f'{int(R)} {int(B)}')
else:
    print('Impossible')
