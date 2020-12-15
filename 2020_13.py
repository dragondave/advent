sample = """939
7,13,x,x,59,x,31,19""".strip()

import input
import math
from functools import reduce

def fake_int(s):
    if s=="x":
        return -1
    else:
        return int(s)

data_raw = input.input(13)
data_raw = input.input(sample)
timestamp = int(data_raw[0])

old_nums = list(int(t) for t in data_raw[1].split(",") if t!="x")
nums = list(fake_int(t) for t in data_raw[1].split(","))

best_wait = 99999999
best_bus = None
#for num in nums:
#    missed_by = timestamp % num
#    if missed_by != 0:
#        time_to_next = num - missed_by
#    else:
#        time_to_next = 0
#    if time_to_next < best_wait:
#        best_bus = num
#        best_wait = time_to_next
#        print (best_bus, best_wait, best_bus*best_wait)


def lcm(x,y):
    return abs(x*y) // math.gcd(x,y)

multiplier = 1
win_time = 0
for minutes_past, bus_number in enumerate(nums):
    if bus_number == -1: continue
    print ("Consider bus ", bus_number)
    while (win_time+minutes_past) % bus_number != 0:
        win_time = win_time + multiplier # align dials
    multiplier = lcm(multiplier, bus_number) # set up skiprate
print (win_time)

