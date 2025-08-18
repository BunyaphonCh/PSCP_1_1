'''How many small brick'''
a = int(input()) # ก้อนเล็ก 4
b = int(input()) # ก้อนใหญ่ 1
goal = int(input()) # ขนาดนิ้วที่ต้อง 9
LENGTH_LARGE = 0
if b < (goal//5):
    LENGTH_LARGE = b * 5 # 5
else:
    LENGTH_LARGE = (goal//5) * 5
REMAIN = goal - LENGTH_LARGE
if REMAIN <= a:
    print(REMAIN)
else:
    print(-1)
