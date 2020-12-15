sample = """
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
""".strip()
import input
import regex
data = input.input(14)
#data = input.input(sample)
#mask = data[0].partition(" = ")[2]

memory = {}
and_num = None
or_num = None
and_mask = None
or_mask = None

def parse(s):
    global and_num, or_num
    if "mask" in s:
        mask = s.partition(" = ")[2]
        and_mask = mask.replace('X', '1') # for 0s
        or_mask = mask.replace('X', '0') # for 1s
        and_num = int(and_mask, 2)
        or_num = int(or_mask, 2)
        return None, None
    loc, val = regex.search(r"mem\[(\d+)\] = (\d+)", s).groups()
    return int(loc), int(val)

for d in data:
    loc, val = parse(d)
    if loc is None:
        print ("MASK", d)
        continue
    #val = val + 2**37

    #print ("value", bin(val))
    #print ("orM..    ", or_mask)
    #print ("=====", bin(val | or_num))
    #print ("andM.    ", and_mask)
    #print ("=====", bin(2**37+(val & and_num) | or_num))
    result = (val & and_num) | or_num
    #print (result)
    memory[loc] = result

print (memory)
print (sum([val for val in memory.values()]))
    

