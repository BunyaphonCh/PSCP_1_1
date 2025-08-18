"""Five M"""
def main():
    """XDD"""
    n = int(input())
    text = ''
    for i in range(1,n+1):
        if not i % 5:
            text += 'X'
        else:
            text += '*'
    print(text)
main()
