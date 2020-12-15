import input

sample = input.input_int("""35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""")

real = input.input_int(9)
data = real # CHANGE ME

if data == sample: # DON'T CHANGE THIS ONE
    preamble = 5
else:
    preamble = 25

print (data[:preamble])


def check_num(i, char):
    prev = data[i:i+preamble]
    #print (prev, char)
    for d in prev:
        if char-d in prev and d+d != char:
            return True
    return False
    
for i, char in enumerate(data[preamble:]):
    if not check_num(i, char):
        print (char)

WEAK = 21806024

begin = 0
end = 0
while True:
    score = sum(data[begin:end])
    if score < WEAK:
        end = end + 1
    elif score > WEAK:
        begin = begin + 1
    else:
        print (score, WEAK, begin, end, min(data[begin:end]), max(data[begin:end])) 
        begin = begin + 1
        end = end + 1