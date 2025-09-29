'''Meteorite'''
def main():
    '''yeahhh'''
    weight = float(input())
    boom = int(input())
    safe_weight = float(input())
    missile_count = 0
    asteroid_count = 1
    while weight >= safe_weight:
        missile_count += asteroid_count
        weight /= boom
        asteroid_count *= boom
    print(missile_count)
main()
