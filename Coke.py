'''What cost dude'''
a = int(input()) # ราคาขวดละ
b = int(input()) # จำนวนฝาที่ใช้เเลก
c = int(input()) # ราคาซื้อขวดใหม่
d = int(input()) # จำนวนโค้กที่ต้องการ
COST_PER_SET = 0
BUY_SET = 0
LEFT = 0
if b == 0 or b > d:
    print(a*d)
else:
    if c == 0:
        COST_PER_SET = b*a
        BUY_SET = d // (b+1)
        LEFT = d % (b+1)
        print((COST_PER_SET*BUY_SET)+(LEFT*a))
    else:
        COST_PER_SET = ((b-1)*a)+c
        BUY_SET = d // b
        LEFT = d % b
        print((COST_PER_SET*BUY_SET)+(LEFT*a))
