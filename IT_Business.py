'''IT Business'''
def main():
    '''it'''
    bank = float(input())
    money = float(input())
    error = 0

    while True:
        txt = input()
        if txt == "end" or error >= 2:
            break
        transaction = txt[0]
        pay = txt[2:]
        pay = float(pay)
        if transaction == "D" and money >= pay:
            bank += pay
            money -= pay
            error = 0
        elif transaction == "W" and bank >= pay:
            bank -= pay
            money += pay
            error = 0
        else:
            error += 1

    print(f'{bank:.2f}')
    print(f'{money:.2f}')

main()
