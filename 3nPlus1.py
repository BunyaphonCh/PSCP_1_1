'''3nPlus1'''
def main():
    '''main func'''


    while True:
        n = int(input())
        count = 0
        if not n:
            break
        while True:
            if n == 1:
                break
            if n % 2:
                n = n * 3 + 1
            else:
                n /= 2
            count += 1

        print(count + 1)

main()
