sample = """
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
""".strip()

sample_2 = """
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
"""

import input
import regex 
bag_lines = input.input(sample)
bag_lines = input.input(7)

def parse_bag(s):
    outer, _, inners = s.partition(" contain ")
    outer = outer.replace(" bags", "")
    inner_options = []
    for bag in inners.split(", "):
        if bag=="no other bags.":
            continue
        num, _, descr = bag.partition(" ")
        num = int(num)
        descr = regex.sub(" bags?\.?", "", descr)
        inner_options.append([descr, num])
    return [outer, inner_options]

bags = {parse_bag(s)[0]:parse_bag(s)[1] for s in bag_lines}
# print (bags)

revbags = {}
for outer, inners in bags.items():
    for inner, count in inners:
        #print (inner)
        if inner not in revbags:
            revbags[inner] = set(((outer, count),))
        else:
            revbags[inner].add((outer, count))

# print (revbags)

search = set(["shiny gold",])
found = set()
known = set()

while search:
    for bag in search:
        try:
            for item, count in revbags[bag]:
                found.add(item)
                known.add(item)
        except KeyError:
            continue
    search = found
    found = set()

# print (len(known))


## part 2

print (bags)
from collections import Counter

class Bag(object):
    def __init__(self, bag):
        self.name = bag
        self.inners = Counter(dict(bags[bag]))
        self.inside = None
    
    def __repr__(self):
        return "{}:{}".format(self.name, self.inners)

    def get_inside(self):
        # how many bags does this bag contain?
        if self.inside is not None:
            return self.inside
        total = 0
        for bag, count in self.inners.items():
            total = total + count*(1+obj_bags[bag].get_inside())
        self.inside = total
        return total

obj_bags = {x:Bag(x) for x in bags}

print (obj_bags['shiny gold'].get_inside())

