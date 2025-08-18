'''encoding'''
def main():
    'count each char'
    result = ''
    count = 1
    text = input() # aaaaahhhhhhmmmmmmmuiiiiiiiaaaaaa
    first = text[0]
    for i,char in enumerate(text):
        if not i: # ข้ามอันที่ 1
            continue
        if char == first:
            count += 1
        else:
            result += str(count) + first
            first = text[i]
            count = 1
    result += str(count) + first
    print(result)
main()
