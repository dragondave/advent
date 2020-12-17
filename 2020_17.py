sample = """
.#.
..#
###
""".strip()

real = """
####...#
......##
####..##
##......
..##.##.
#.##...#
....##.#
.##.#.#.
""".strip()

import input
import numpy as np
MAX = 21
mid = (MAX -1) // 2
grid = np.zeros([MAX, MAX, MAX, MAX], dtype=int)
flat = input.input_grid(real, ".#")
print (flat)
size = len(flat[0])
offset = size // 2
for x in range(len(flat[0])):
    for y in range(len(flat[0])):
        grid[mid][mid][mid+x-offset][mid+y-offset] = flat[x][y]

print(grid[mid][mid])

def iterate_life(life):
    new_life = np.zeros([MAX,MAX,MAX,MAX], dtype=int)
    
    for x in range(MAX):
        for y in range(MAX):
            for z in range(MAX):
                for w in range(MAX):
                    score = 0
                    for xx in [-1, 0, 1]:
                        for yy in [-1, 0, 1]:
                            for zz in [-1, 0, 1]:
                                for ww in [-1, 0, 1]:
                                    if xx == 0 and yy == 0 and zz == 0 and ww == 0: continue
                                    newx = x+xx
                                    newy = y+yy
                                    newz = z+zz
                                    neww = w+ww
                                    if newx < 0 or newy < 0 or newz < 0 or neww < 0: continue
                                    if newx >= MAX or newy >= MAX or newz >= MAX or neww >= MAX: continue
                                    score = score+life[newx][newy][newz][neww]
                    if score == 3:
                        new_life[x][y][z][w] = 1
                    if score == 2:
                        new_life[x][y][z][w] = life[x][y][z][w]
    return new_life

grid = iterate_life(grid)
print (grid[mid][mid])
print (np.count_nonzero(grid))

grid = iterate_life(grid)
grid = iterate_life(grid)
#print (grid[mid][mid])
#
grid = iterate_life(grid)
grid = iterate_life(grid)
grid = iterate_life(grid)
print (np.count_nonzero(grid))
#print (grid[mid])
    # part 2
    #new_life[0][0] = 1
    #new_life[0][MAX-1] = 1
    #new_life[MAX-1][0] = 1
    #new_life[MAX-1][MAX-1] = 1