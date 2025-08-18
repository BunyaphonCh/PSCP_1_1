'''Sum of number'''
def main():
    '''XDD'''
    summ = int(input()) # 100
    count_sum = 0
    while True:
        if count_sum == summ:
            break
        n = int(input())
        if n == -1:
            break
        count_sum += n
    print(count_sum)
main()
