'''Hew ah'''
word1 = input()
word2 = input()
DISTANCE = 0
for i,j in zip(word1,word2):
    if i != j:
        DISTANCE += 1
print(DISTANCE)
