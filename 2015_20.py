real = 34000000

from sympy import factorint
from itertools import combinations
import numpy as np

house = 1024

def get_elves(house):
    factors = factorint(house)
    factor_list = []
    for factor, copies in factors.items():
        factor_list.extend([factor] * copies)
    
    combination_list = []
    for x in range(0, len(factor_list)+1):
        combination_list.extend(combinations(factor_list, x))
    
    elves = set([int(np.product(np.array(c))) for c in combination_list])
    elves = [x for x in elves if x*50>=house]
    return sum(elves)*11


print (get_elves(720720))
#house = 370000
house = 720720 # https://oeis.org/A002182
while True:
    house += 1
    if get_elves(house) > real:
        print (house)
        break
    if house % 1000 == 0:
        print (house)