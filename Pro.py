'''Pro'''
def main():
    '''Pro'''
    kon = int(input()) # 4
    jai = int(input()) # 3
    price_person = int(input()) # 100
    all_person = int(input()) # 8
    res = price_person * all_person # 100 * 8 = 800
    if all_person >= kon: # 8 >= 4
        free = kon-jai # 5-2 = 3
        num_free = (all_person // kon) * free # 12//5 -> 2 * 3 = 6
        discount = num_free * price_person # 6 * 100
        res = res - discount # 800 - 200 = 600
    print(res)
main()
