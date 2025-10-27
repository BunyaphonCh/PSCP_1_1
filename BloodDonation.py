'''BloodDonation'''
def main():
    '''BloodDonation'''
    age = int(input()) # 58
    weight = int(input()) # 60
    times = int(input()) # 12
    state = False
    if weight >= 45 and 17 <= age <= 70:
        if age == 17 or 60 <= age <= 70:
            agree = input().capitalize()
            if ((60 <= age <= 70) and times) or age == 17:
                state = agree == 'True'
        elif (not times and age < 55) or (times):
            state = True
    print('Yes' if state else 'No')
main()
