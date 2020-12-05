import numpy as np
import input

# 865 too low

sample = """
.#.#.#
...##.
#....#
..#...
#.#..#
####..
"""

np.set_printoptions(threshold=999999, linewidth=999999)
life_raw = (input.input(18, 2015))
MAX = 100
STEPS = 100

#life_raw = input.input(sample)
#MAX = 6
#STEPS = 4

life = np.array([list(x) for x in life_raw])
life[life=='#'] = 1
life[life=='.'] = 0
life = life.astype('int')
# print (life)

life[0][0] = 1
life[0][MAX-1] = 1
life[MAX-1][0] = 1
life[MAX-1][MAX-1] = 1
    
def iterate_life(life):
    new_life = np.zeros([MAX,MAX], dtype=int)
    
    for x in range(MAX):
        for y in range(MAX):
            score = 0
            for xx in [-1, 0, 1]:
                for yy in [-1, 0, 1]:
                    if xx == 0 and yy == 0: continue
                    newx = x+xx
                    newy = y+yy
                    if newx < 0 or newy < 0: continue
                    if newx >= MAX or newy >= MAX: continue
                    score = score+life[newx][newy]
            if score == 3:
                new_life[x][y] = 1
            if score == 2:
                new_life[x][y] = life[x][y]

    # part 2
    new_life[0][0] = 1
    new_life[0][MAX-1] = 1
    new_life[MAX-1][0] = 1
    new_life[MAX-1][MAX-1] = 1
    

    return new_life

for i in range(STEPS):
    life = iterate_life(life)
    print (np.sum(life))
    #print (life)