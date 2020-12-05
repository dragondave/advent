import input
from numpy import array

real = input.input_raw(3, 2015)

sample = "^>v<"

directions = {
    "^": array([0,+1]),
    "v": array([0,-1]),
    "<": array([-1, 0]),
    ">": array([+1, 0]),
}


deliver = 1
pos = [array([0,0]), array([0,0])]
houses = set([str(pos[0])])
active = 0
for char in real:
    pos[active] = pos[active] + directions[char]
    if str(pos[active]) not in houses:
        deliver += 1
        houses.add(str(pos[active]))
    print (deliver, str(pos[active]))
    active = 1 - active

