'''Donut'''
def main():
    '''Donut
    ต้องจ่ายเงินน้อยสุดกี่สุด ได้โดนัทมากสุดกี่ชิ้น'''
    price = int(input()) # 5
    amount = int(input()) # 3
    free = int(input()) # 1
    want_least = int(input()) # 8
    current_donut = 0
    current_free = 0
    while (current_donut + current_free) < want_least:
        current_donut += 1
        if current_donut and not current_donut % amount:
            current_free += free
    print(current_donut * price, current_donut + current_free)
main()
