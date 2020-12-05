import regex
import input
import numpy as np
sample = """
Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
""".strip()

# less than 20428800

sample = np.array((
    [-1, -2,  6,  3, 8],
    [ 2,  3, -2, -1, 3],
)).transpose()

real = np.array((
    [2, 0, -2, 0, 3],
    [0, 5, -3, 0, 3],
    [0, 0,  5, -1, 8],
    [0, -1, 0, 5, 8]
)).transpose()

data = real

def score(amounts):
    x = amounts * data
    q = np.sum(x, 1)
    q = q[:-1]
    q[q<0] = 0
    qq = np.product(q)
    return qq

# print (score(np.array([44, 56])))

def new_amounts(amounts):
    for i in range(len(amounts)):
        for j in range(len(amounts)):
            if i==j: continue
            new = np.copy(amounts)
            new[i] += 1
            new[j] -= 1
            yield new

def calorie_control(amounts):
    new = np.copy(amounts)
    new[0] += 1
    new[1] -= 1
    yield new
    new = np.copy(amounts)
    new[1] += 1
    new[0] -= 1
    yield new
    new = np.copy(amounts)
    new[2] += 1
    new[3] -= 1
    yield new
    new = np.copy(amounts)
    new[3] += 1
    new[2] -= 1
    yield new

def search():
    amounts = np.array([30, 30, 31, 9])
    max_ing = True
    while max_ing is not None:
        max_sat = score(amounts)
        max_ing = None
        for a in calorie_control(amounts):
            s = score(a)
            if s>max_sat:
                max_sat = s
                max_ing = a
                print (s, a)
        amounts = max_ing
    
    
print (search())