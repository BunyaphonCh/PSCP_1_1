'''Bubble Tea''' 

PEARL_ENERGY = {
    'H' : 5,
    'O' : 3,
    'J' : 2 
}

TEA_ENERGY = {
    'R' : {1:12, 2:18, 3:25},
    'T' : {1:15, 2:20, 3:30},
    'M' : {1:10, 2:15, 3:20}
}

def main():
    '''Bubble Tea'''
    pearl, quantity = input().split()
    tea, sweet, volume = input().split()
    energy = 0
    quantity = int(quantity)
    volume = int(volume)
    sweet = int(sweet)
    energy += PEARL_ENERGY.get(pearl, 0) * quantity
    energy += TEA_ENERGY.get(tea, {}).get(sweet, 0) * volume
    print(energy)
main()
