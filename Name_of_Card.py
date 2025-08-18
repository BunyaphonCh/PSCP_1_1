'''Card'''
name = input()
RESULT = ''
if name[:1] == 'A' or name[:1] == 'a':
    RESULT += 'Ace of '
elif name[:1] == 'J' or name[:1] == 'j':
    RESULT += 'Jack of '
elif name[:1] == 'Q' or name[:1] == 'q':
    RESULT += 'Queen of '
elif name[:1] == 'K' or name[:1] == 'k':
    RESULT += 'King of '
else:
    if len(name) == 3:
        RESULT += '10 of '
        if name[2:] == 'D' or name[2:] == 'd':
            RESULT += 'Diamonds'
        elif name[2:] == 'H' or name[2:] == 'h':
            RESULT += 'Hearts'
        elif name[2:] == 'S' or name[2:] == 's':
            RESULT += 'Spades'
        elif name[2:] == 'C' or name[2:] == 'c':
            RESULT += 'Clubs'
    else:
        RESULT += name[:1] + ' of '
if name[1:] == 'D' or name[1:] == 'd':
    RESULT += 'Diamonds'
elif name[1:] == 'H' or name[1:] == 'h':
    RESULT += 'Hearts'
elif name[1:] == 'S' or name[1:] == 's':
    RESULT += 'Spades'
elif name[1:] == 'C' or name[1:] == 'c':
    RESULT += 'Clubs'
print(RESULT)
