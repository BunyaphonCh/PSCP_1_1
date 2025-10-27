'''Inflation'''
def main():
    '''Inflation'''
    n = input().strip()
    k = int(input())
    baht = 0
    satang = 0
    if '.' in n:
        part = n.split('.')
        baht = int(part[0]) if part[0] else 0
        satang = int(part[1][:2].ljust(2,'0'))
        satang = int(satang)
    else:
        baht = int(n) if n else 0
        satang = 0
    price = (baht * 100) + satang
    for _ in range(k):
        increase_satang = (price * 381) // 10000
        price += increase_satang
    final_baht = price // 100
    final_satang = price % 100
    print(f'{final_baht}.{final_satang:02d}')
main()
