'''CoinChangev1'''
def main():
    '''CoinChangev1'''
    money = int(input())
    total_coin = 0
    change = 0
    total_coin += (money // 25)
    change = money % 25
    total_coin += (change // 10)
    change = change % 10
    total_coin += (change // 5)
    change = change % 5
    total_coin += (change // 1)
    change = change % 1
    print(total_coin)
main()
