"""what color"""
c1 = input()
c2 = input()
RESULT = 'Error'
if ((c1 == 'Red' and c2 == 'Yellow') or (c2 == 'Red' and c1 == 'Yellow')):
    RESULT = 'Orange'
elif ((c1 == 'Red' and c2 == 'Blue') or (c2 == 'Red' and c1 == 'Blue')):
    RESULT = 'Violet'
elif ((c1 == 'Yellow' and c2 == 'Blue') or (c2 == 'Yellow' and c1 == 'Blue')):
    RESULT = 'Green'
elif (c1 == 'Red' and c2 == 'Red'):
    RESULT = 'Red'
elif (c1 == 'Yellow' and c2 == 'Yellow'):
    RESULT = 'Yellow'
elif (c1 == 'Blue' and c2 == 'Blue'):
    RESULT = 'Blue'
print(RESULT)
