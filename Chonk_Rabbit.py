'''Bit Kub'''
def main():
    '''rabbit'''
    num = int(input())
    over = 0
    name_max = 0
    weight_max = 0
    for _ in range(num):
        name, weight = input().split()
        weight = int(weight)
        if weight > 15:
            over += 1
        if weight > weight_max:
            weight_max = weight
            name_max = name
    print(over)
    print(f'{name_max} {weight_max}')
main()
