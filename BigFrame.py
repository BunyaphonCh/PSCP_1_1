'''big frame'''
def main():
    '''big big frame'''
    a = input().strip()
    b = input().strip()
    c = input().strip()
    d = input().strip()
    e = input().strip()

    lenght = max(len(a), len(b), len(c), len(d), len(e))

    print("*" * (lenght + 4))
    print(f'* {a:<{lenght}} *')
    print(f'* {b:<{lenght}} *')
    print(f'* {c:<{lenght}} *')
    print(f'* {d:<{lenght}} *')
    print(f'* {e:<{lenght}} *')
    print("*" * (lenght + 4))

main()
