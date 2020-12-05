sample = """
Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.
""".strip()

import input
import regex
from itertools import permutations

data = input.input(13, 2015)

def parseline(s):
    gainsign = {'gain': +1, 'lose': -1}
    n1,gainlose,happy,n2 = regex.search(r"(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+)\.", s).groups()
    happyint = int(happy)*gainsign[gainlose]
    return n1, n2, happyint

nicedata = [parseline(l) for l in data]
people = set(n[0] for n in nicedata)
# part 2
# people.add("Me")
perms = permutations(people)
happy = {(n1, n2): score for n1, n2, score in nicedata}
print (happy)

def scoreperm(table):
    score = 0
    table = list(table)
    table.append(table[0])
    print (table)
    for i in range(len(table)-1):
        if table[i] != "Me" and table[i+1] != "Me":
            score = score + happy[(table[i], table[i+1])]
            score = score + happy[(table[i+1], table[i])]
    return score

max_score = -9999999
max_arr = None
for p in perms:
    score = scoreperm(p)
    if score > max_score:
        max_score = score
        max_arr = p

print (max_score, max_arr)




