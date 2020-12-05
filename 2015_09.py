sample = """
London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
"""

# > 674
import input
import regex
from itertools import permutations

data = {}
for row in input.input(9, 2015):
    c1, c2, dist = regex.search(r"^(\w+) to (\w+) = (\d+)$", row).groups()
    data[(c1, c2)] = int(dist)
    data[(c2, c1)] = int(dist)

cities = set()
for d in data:
    cities.add(d[0])

mindist = -1
minpath = None
for perm in permutations(cities):
    dist = 0
    for i in range(len(cities)-1):
        print (perm[i], perm[i+1])
        dist = dist + data[(perm[i], perm[i+1])]
    print (dist)
    if dist > mindist:
        minpath = perm
        mindist = dist

print (minpath, mindist)
