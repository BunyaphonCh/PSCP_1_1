"""I want to eat buffet"""
x = int(input()) # มา x คน 4
y = int(input()) # จ่าย y คน
a = int(input()) # ราคาต่อคน a บาท
z = int(input()) # ทาน z คน จ่ายเท่าไหร่
price = z*a
if x <= z:
    free = x-y
    num_free = (z // x) * free
    discount = num_free * a
    price =  price - discount
print(price)
