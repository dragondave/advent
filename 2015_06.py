import regex
import input

# 485167: too high

sample = """
turn on 0,0 through 999,999
toggle 0,0 through 999,0
turn off 499,499 through 500,500
"""

import numpy
lights = numpy.tile(0, (1000,1000))

def parse(s):
    coords = regex.search(r" (\d+),(\d+) through (\d+),(\d+)$", s).groups()
    for w, f in functions.items():
        if w in s:
            function = f
    return function, list([int(x) for x in coords])

def toggle(x,y):
    lights[x][y] += 2
    
def on(x,y):
    lights[x][y] += 1
    
def off(x,y):
    lights[x][y] -= 1
    lights[x][y] = max(lights[x][y], 0)

functions = {
    "turn on": on,
    "turn off": off,
    "toggle": toggle
}

def execute(s):
    print (s)
    f, coords = parse(s)
    print (f, coords)
    minx, miny, maxx, maxy = coords

    for x in range(minx, maxx+1):
        for y in range(miny, maxy+1):
            f(x,y)

for r in input.input(6, 2015):
    execute(r)
    print (numpy.sum(lights))
    

