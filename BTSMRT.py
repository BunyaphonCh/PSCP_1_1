'''BTSMRT'''
def main():
    '''BTSMRT
    เด็กกว่า -> สูงต่ำกว่า 90 cm -> ขึ้นฟรีทุกวัน
    เด็ก -> อายุต่ำกว่า 14 ปี เเละ สูงไม่เกิน 140 cm -> ขึ้นฟรีในวันเด็ก , วันอื่นได้ส่วนลด
    ผู้สูงอายุ -> อายุ 60 ปีขึ้นไป -> ขึ้นฟรีวันผู้สูงอายุ , วันอื่นได้ส่วนลด
    นอกนั้นจ่ายปกติ'''
    category = input()
    age = float(input())
    height = float(input())
    very_child = (age < 14) & (height < 90)
    child = (age < 14) & (height <= 140) & (category == 'Children Day')
    elder = (age >= 60) & (category == 'Senior Day')
    if very_child:
        print('FREE')
    elif child:
        print('FREE')
    elif elder:
        print('FREE')
    else:
        print('PAY')
main()
