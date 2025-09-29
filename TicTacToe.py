'''tic_Tac_Toe'''
def main():
    '''TicTacToe'''
    # [['O', 'X', 'O'], ['X', 'O', 'X'], ['O', 'X', 'O']]
    res = 'DRAW'
    row1 = input()
    row2 = input()
    row3 = input()
    n00,n01,n02 = row1
    n10,n11,n12 = row2
    n20,n21,n22 = row3
    if n00 == n01 == n02: # check row
        if n00 not in ('-',' '):
            res = f'{n01} WIN'
    elif n10 == n11 == n12: # check row
        if n11 not in ('-',' '):
            res = f'{n11} WIN'
    elif n20 == n21 == n22: # check row
        if n21 not in ('-',' '):
            res = f'{n21} WIN'
    elif n00 == n10 == n20: # check column
        if n10 not in ('-',' '):
            res = f'{n10} WIN'
    elif n01 == n11 == n21: # check column
        if n11 not in ('-',' '):
            res = f'{n11} WIN'
    elif n02 == n12 == n22: # check column
        if n12 not in ('-',' '):
            res = f'{n12} WIN'
    elif n00 == n11 == n22:
        if n00 not in ('-',' '):
            res = f'{n00} WIN'
    elif n02 == n11 == n20:
        if n02 not in ('-',' '):
            res = f'{n02} WIN'
    print(res)
main()
