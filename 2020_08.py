sample = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

import input
from time import sleep
from copy import deepcopy

data = input.input(8)
#data = input.input(sample)

data = [d.split(" ") for d in data]
data = [[d[0], int(d[1])] for d in data]
# print (data)

def test(data):
    pc = 0
    acc = 0
    visited = set()
    while True:
        try:
            op, num = data[pc]
        except IndexError:
            return acc
        #print (pc, data[pc])
        if op == "acc":
            pc = pc + 1
            if pc in visited:
                raise RuntimeError
            visited.add(pc)
            acc = acc + num
        elif op == "jmp":
            pc += num
            if pc in visited:
                raise RuntimeError
            visited.add(pc)
            
        elif op == "nop":
            pc = pc + 1
            if pc in visited:
                raise RuntimeError
            visited.add(pc)
            
        else:
            raise RuntimeError
        #sleep (.2)
    return num
        
for i in range(len(data)):
    newdata = deepcopy(data)
    if newdata[i][0] == "nop":
        newdata[i][0] = "jmp"
    elif newdata[i][0] == "jmp":
        newdata[i][0] = "nop"
    else:
        continue

    #print (data)

    try:
        num = test(newdata)
    except RuntimeError:
        continue
    else:
        print (num, "!")
        print (newdata)

# < 1614