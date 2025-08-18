'''align'''
def main():
    '''main func'''
    size = int(input())
    command = input()
    txt = input().strip()
    if command == "left":
        print(f'{txt:<{size}}')
    elif command == "center":
        if (not size % 2 and len(txt) % 2) or (size % 2 and not len(txt) % 2):
            print(f' {txt:^{size - 1}}')
        else:
            print(f'{txt:^{size}}')
    elif command == "right":
        print(f'{txt:>{size}}')

main()
