'''efesfs'''
def main():
    'ewfwewe'
    n = int(input()) # 3
    for i in range(1,n+1): # 0 1 2
        for j in range(2*(n-i),1,-1):
            print(' ',end='')
        for j in range(1,i+1):
            print(f'{j:02}',end=' ')
        print()
main()
