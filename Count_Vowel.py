"""Count vowel"""
def main():
    """NO PEP-8"""
    n = int(input())
    count = 0
    lis = []
    for _ in range(n):
        char = input()
        lis.append(char)
    for i in lis:
        if i in ('A','E','I','O','U','a','e','i','o','u'):
            count += 1
    print(count)
main()
