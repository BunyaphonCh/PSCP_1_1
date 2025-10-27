'''Progressive tax'''
def main():
    '''Progressive tax'''
    money = int(input())
    tax = 0
    damn_rule = [
        (10000, 0.10),
        (20000, 0.15),
        (30000, 0.20)
    ]
    for amount, rate in damn_rule:
        if money <= 0:
            break
        tax_amount = min(money, amount)
        tax += tax_amount * rate
        money -= tax_amount
    if money > 0:
        tax += money * 0.25
    print(f'{tax:.1f}')
main()
