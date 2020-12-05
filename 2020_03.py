sample = """
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""

import input
import numpy as np
np.set_printoptions(threshold=999999, linewidth=999999)
sample = input.input_grid(sample)
real = input.input_grid(3, 2020)
data = real

width = len(data[0])
height = len(data)
print (data)
print (width, height)

xpos = 0
ypos = 0

def get_tree(x, y):
    return data[y][x%width]

def slope(xskip, yskip):
    count = 0
    for y in range(height):
        if y%yskip:
            continue
        x = int(y*(xskip/yskip))
        count += get_tree(x, y)
    return count

a = slope(1,1)
b= slope(3,1)
c= slope(5,1)
d= slope(7,1)
e=slope(1,2)
print (a*b*c*d*e)

