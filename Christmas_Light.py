'''That light brigther than ma life'''
COLORS = ['Red','Green','Blue']
MAP = {"R": 0, "G": 1, "B": 2}
start = input()
times = int(input())
START_INDEX = MAP[start]
RESULT = ''
for i in range(times):
    RESULT += (str(COLORS[((START_INDEX+i)%3)]) + ' ')
print(RESULT)
