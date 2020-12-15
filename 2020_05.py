"""7 FB -> 128 rows
3 LR -> 8 cols
seat id = row*8+col"""

import input
passes = input.input(5, 2020)

def parse_pass(s):
    s = s.replace("F", "0")
    s = s.replace("B", "1")
    s = s.replace("L", "0")
    s = s.replace("R", "1")
    row = int(s[:7], 2)
    col = int(s[7:], 2)

    return (row*8 + col)


hi = 0
lo = 9999
seats = []
for bpass in passes:
    seat = parse_pass(bpass)
    seats.append(seat)
    hi = max(hi, seat)
    lo = min(lo, seat)

for i in range(lo, hi):
    if i not in seats:
        print("**", i)
print (lo, hi)

