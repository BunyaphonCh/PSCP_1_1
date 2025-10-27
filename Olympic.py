'''Olympic'''
def sort(item):
    '''Olympic'''
    name = item[0]
    medal = item[1]
    return (-medal[0], -medal[1], -medal[2], name)

def main():
    '''Olympic'''
    num = int(input())
    data = {}
    rank_real = 1
    rank_show = 1
    pre_medal = [0,0,0]
    for _ in range(num):
        text = input().split()
        data[text[0]] = text[1:]
    sorted_data = [
        (name, list(map(int, medal)))
        for name, medal in data.items()
    ]
    sorted_data.sort(key=sort)
    for rank_real, (name, medal) in enumerate(sorted_data, start=1):
        if medal != pre_medal:
            rank_show = rank_real
        total = sum(medal)
        medal_str = ' '.join(map(str, medal))
        print(f'{rank_show} {name} {medal_str} {total}')
        pre_medal = medal
main()
