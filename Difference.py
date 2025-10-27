'''Difference'''
def main():
    '''Difference'''
    n = int(input())
    m = int(input())
    A = set()
    B = set()
    for _ in range(n):
        num = int(input())
        A.add(num)
    for _ in range(m):
        num = int(input())
        B.add(num)
    list_ya = sorted(list(A-B))
    print(*list_ya)
main()
