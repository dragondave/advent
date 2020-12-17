sample = """
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
""".strip()
import input
import regex
import itertools
data = input.input(14)
#data = input.input(sample)
#mask = data[0].partition(" = ")[2]

memory = {}
mask = None
and_num = None
or_num = None
and_mask = None
or_mask = None
notx_mask = None
notx_num = None

def parse(s):
    global and_num, or_num, mask, notx_num
    if "mask" in s:
        mask = s.partition(" = ")[2]
        and_mask = mask.replace('X', '1') # for 0s
        or_mask = mask.replace('X', '0') # for 1s
        notx_mask = mask.replace("0", "1").replace("X", "0")
        and_num = int(and_mask, 2)
        or_num = int(or_mask, 2)
        notx_num = int(notx_mask, 2)
        return None, None
    loc, val = regex.search(r"mem\[(\d+)\] = (\d+)", s).groups()
    return int(loc), int(val)

def floating_mask(s):
    positions = [35-x.span()[0] for x in regex.finditer("X", s)] # 0..35
    values = [2**n for n in positions]
    for width in range(0, len(values)+1):
        for combo in itertools.combinations(values, width):
            yield sum(combo)
    


print ("BEGIN")
for d in data:
    loc, val = parse(d)
    if loc is None:
        floating = list(floating_mask(mask))
        continue
    #val = val + 2**37

    #print ("value", bin(val))
    #print ("orM..    ", or_mask)
    #print ("=====", bin(val | or_num))
    #print ("andM.    ", and_mask)
    #print ("=====", bin(2**37+(val & and_num) | or_num))
    result = (val & and_num) | or_num
    #print (result)
    print (loc, or_num)
    print ("!", bin(loc), bin(or_num), bin(notx_num))
    memory_zero = (loc | or_num) & notx_num
    print ("MEMO", memory_zero)
    locs = [f + memory_zero for f in floating]
    print ("write {} to {}".format(result, locs))
    
    for m in locs:
        memory[m] = val

print (memory)
print (sum([val for val in memory.values()]))
    

# 2201613694753258 too high
# 4330547254348