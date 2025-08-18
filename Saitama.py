"""I'm gonna be Saitama"""
import math
pushup = int(input())
situp = int(input())
squat = int(input())
run = int(input())
pushup_day = int(input())
situp_day = int(input())
squat_day = int(input())
run_day = int(input())
pushup_result = math.ceil(pushup / pushup_day)
situp_result = math.ceil(situp / situp_day)
squat_result = math.ceil(squat / squat_day)
run_result = math.ceil(run / run_day)
high_day = pushup_result
if high_day < situp_result:
    high_day = situp_result
if high_day < squat_result:
    high_day = squat_result
if high_day < run_result:
    high_day = run_result
print(high_day)
