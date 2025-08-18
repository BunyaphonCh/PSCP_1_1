"""How much i have to paid ?"""
price = int(input())
SERVICE = price * 0.1
if SERVICE < 50:
    SERVICE = 50
elif SERVICE > 1000:
    SERVICE = 1000
vat = (price + SERVICE) * 0.07
paid = price + SERVICE + vat
print(f'{paid:.2f}')
