'''RuleOfThree'''
def main():
    '''RuleOfThree
    size / price ยิ่งมาก -> คุ้ม
    เเสดงผลว่าซื้ออันไหนคุ้มที่สุด ถ้าคุ้มเท่ากัน ให้เลือกที่ราคาต่ำกว่า'''
    num = int(input())
    res_size = 0
    res_price = 0
    latest_cal = 0
    for _ in range(num): # 2
        size = float(input()) # 15 | 39
        price = float(input()) # 53 | 160
        cal = price / size # 3.53 | 4.10
        if (cal > latest_cal) or (cal == latest_cal and res_price > price):
            latest_cal = cal # 4.10
            res_size = size # 39
            res_price = price # 160
    print(f'{res_size:.2f} {res_price:.2f}')
main()
