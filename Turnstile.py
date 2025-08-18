'''Turnstile'''
LOCKED = True
COUNT = 0
while True:
    action = input()
    if action == 'END':
        break
    if action == 'C':
        LOCKED = False
    if LOCKED is False and action == 'P':
        COUNT += 1
        LOCKED = True
print(COUNT)
