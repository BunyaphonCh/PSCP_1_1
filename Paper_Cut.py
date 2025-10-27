'''paper cut'''
def main():
    '''paper cut'''
    W,H = input().split()
    _,_ = input().split()
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    x_lis = []
    y_lis = []
    x = [0] + x + [int(W)]
    y = [0] + y + [int(H)]
    all_area = []
    x_lis = [x[i] - x[i-1] for i in range(1, len(x))]
    y_lis = [y[i] - y[i-1] for i in range(1, len(y))]
    for i in x_lis:
        for j in y_lis:
            all_area.append(i*j)
    all_area.sort(reverse=True)
    print(all_area[0])
    print(all_area[1])
main()
