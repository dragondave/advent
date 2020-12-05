sample = """
20
15
10
5
5
"""

real = """
50
44
11
49
42
46
18
32
26
40
21
7
18
43
10
47
36
24
22
40"""

MAX = 150

import input
from itertools import combinations
data = sorted(input.input_int(real))

print (data)

def make_amount():
    options = []
    for bucket in data:
        new_options  = []
        for option_vol, option_buckets in options:
            new_amount = option_vol + bucket
            if new_amount <=MAX:
                new_options.append([new_amount, option_buckets+1])
        options.extend(new_options)
        options.append([bucket, 1])
    filled = [x for x in options if x[0] == MAX and x[1]==4]
    #print (options.count(MAX))
    print (len(filled))
    most=999
    for f in filled:
        if f[1]<most:
            most=f[1]

    print(most)
    #print(options)

make_amount()