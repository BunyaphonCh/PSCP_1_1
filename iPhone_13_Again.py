'''iPhone 13 Again'''
def main():
    '''iPhone 13 Again'''
    model = input()
    capacity = input().replace(' ','')
    if model == 'iPhone 13 mini':
        dict_mod = {'128GB':25900,'256GB':29900,'512GB':37900}
    elif model == 'iPhone 13':
        dict_mod = {'128GB':29900,'256GB':33900,'512GB':41900}
    elif model == 'iPhone 13 Pro':
        dict_mod = {'128GB':38900,'256GB':42900,'512GB':50900,'1TB':58900}
    elif model == 'iPhone 13 Pro Max':
        dict_mod = {'128GB':42900,'256GB':46900,'512GB':54900,'1TB':62900}
    else:
        print('Not Available')
        return
    print(dict_mod.get(capacity,'Not Available'))
main()
