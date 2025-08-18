'''Weight pig'''
num = int(input()) # 3
pair = input().split() # 1 3 4 7 8 9
WEIGHT = [int(w) for w in pair]
FORMULA = ''
RESULT = 0
if num == 1:
    if WEIGHT[0] > WEIGHT[1]:
        FORMULA = str(WEIGHT[0])
    elif WEIGHT[1] > WEIGHT[0]:
        FORMULA = str(WEIGHT[1])
else:
    for i in range(num): # 0 1 2
        if not i:
            if WEIGHT[i] < WEIGHT[i+1]:
                RESULT += WEIGHT[i+1]
                if (i+1) == num:
                    FORMULA += str(WEIGHT[i+1])
                else:
                    FORMULA += str(WEIGHT[i+1]) + ' + '
            else:
                RESULT += WEIGHT[i]
                if (i+1) == num:
                    FORMULA += str(WEIGHT[i])
                else:
                    FORMULA += str(WEIGHT[i]) + ' + '
        else:
            if WEIGHT[i*2] < WEIGHT[(i*2)+1]:
                RESULT += WEIGHT[(i*2)+1]
                if (i+1) == num:
                    FORMULA += str(WEIGHT[(i*2)+1])
                else:
                    FORMULA += str(WEIGHT[(i*2)+1]) + ' + '
            else:
                RESULT += WEIGHT[i*2]
                if (i+1) == num:
                    FORMULA += str(WEIGHT[i*2])
                else:
                    FORMULA += str(WEIGHT[i*2]) + ' + '
    FORMULA += ' = ' + str(RESULT)
print(FORMULA)
