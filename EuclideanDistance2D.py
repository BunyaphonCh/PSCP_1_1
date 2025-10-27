"""Find distance by using euclidean between"""
def main():
    '''euclidean'''
    q1 = float(input())
    q2 = float(input())
    p1 = float(input())
    p2 = float(input())
    cal = (((q1-p1) ** 2) + ((q2-p2) ** 2)) ** 0.5
    print(cal)
main()
