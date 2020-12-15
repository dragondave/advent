# L empty

import input
import numpy as np
from copy import deepcopy
sample = """
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
""".strip()

debug = False
data = input.input_grid(sample, symbols='.L')
data = input.input_grid(11, symbols = '.L')

class State(object):
    def __init__(self, data, targets = None):
        self.data = data
        self.maxy = np.size(data, axis=0)
        self.maxx = np.size(data, axis=1)
        if targets is None:
            self.targets = {}
        else:
            self.targets = targets

    def at(self, x, y):
        return self.data[y][x]
    
    def count_occ(self, x, y):
        total = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                xx = x + dx
                yy = y + dy
                if xx < 0 or yy < 0:
                    continue
                if xx==x and yy==y:
                    continue
                if xx >=self.maxx or yy >= self.maxy:
                    continue
                if debug:
                    print (xx,yy, self.at(x,y))
                if self.at(xx,yy) == 2:
                    total = total + 1
        return total
    
    def count_scan(self, x, y):
        total = 0
        for target in self.targets[(x,y)]:
            if debug:
                print (target)
            if self.at(target[0], target[1]) == 2:
                total = total + 1
        return total

    def scan(self, x,y):
        targets = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                offset = 0
                while True:
                    offset = offset + 1
                    xx = x + (dx*offset)
                    yy = y + (dy*offset)
                    if xx < 0 or yy < 0:
                        break
                    if xx >= self.maxx or yy >= self.maxy:
                        break
                    if self.at(xx,yy) > 0:
                        targets.append((xx,yy))
                        break
                    
        self.targets[(x,y)] = targets

    def next_state(self):
        newstate = State(deepcopy(self.data), targets=self.targets)
        for x in range(self.maxx):
            for y in range(self.maxy):
                seat = self.at(x,y)
                # count_occ for part 1
                occ = self.count_scan(x,y)
                if seat == 0:
                    continue
                elif seat == 1 and occ == 0:
                    newstate.data[y][x] = 2
                # 4 for part 1
                elif seat == 2 and occ >= 5:
                    newstate.data[y][x] = 1
        return newstate

    def full_scan(self):
        for x in range(self.maxx):
            for y in range(self.maxy):
                self.scan(x,y)

    def __repr__(self):
        return str(self.data)

s = State(data)
s.full_scan()
while True:
    s = s.next_state()
    people = np.count_nonzero(s.data == 2)
    print (people)

