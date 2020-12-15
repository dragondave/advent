sample = """16
10
15
5
1
11
7
19
6
12
4"""

sample_2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

import input
from collections import Counter
sample = input.input_int(sample)
sample_2 = input.input_int(sample_2)
real = input.input_int(10)
data = real


data.extend([0, max(data)+3])
sdata = sorted(data)
counter = Counter()
for i in range(len(sdata)-1):
    counter[sdata[i+1] -sdata[i]] += 1

print (counter)

perms = Counter({0: 1})
for i in range(1, max(sdata)+1):
    s = 0
    for j in [i-1, i-2, i-3]:
        if j in sdata and i in sdata:
            s = s + perms[j]
    perms[i] = s

print (perms[max(sdata)])


