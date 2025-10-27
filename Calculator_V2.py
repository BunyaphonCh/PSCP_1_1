'''Calculator V2'''
def main():
    '''Calculator V2'''
    n = int(input()) # 123
    ori = n
    res = 0
    digit = 1
    count = 9
    if n == 1:
        res = 1
    else:
        while n > 0:
            if n >= count: # 123 >= 9 | 114 >= 90
                res += count * digit # 9 * 1 = 9 | 90 * 2 = 180
                n -= count # 123 - 9 = 114 | 114 - 90 = 24
                digit += 1 # 2 | 3
                count *= 10 # 90 | 900
            else: # 24
                res += n * digit
                n = 0
        res += ori
    print(res)
main()
