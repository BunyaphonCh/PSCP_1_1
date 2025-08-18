"""Go market"""
n = input()
carrot, cabbage, tomato = n.split()
carrot_price = int(carrot) * 10
cabbage_price = int(cabbage) * 25
tomato_price = int(tomato) * 3
pay = carrot_price + cabbage_price + tomato_price
print(pay)
