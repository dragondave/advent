ticker = """
children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1
"""

import input
import regex
ticker = input.input(ticker)
sues = input.input(16,2015)

def parse_ticker():
    ticker_output = {}
    for t in ticker:
        name, quantity = regex.search(r'(\w+): (\d+)', t).groups()
        ticker_output[name] = int(quantity)
    return ticker_output

ticker_output = parse_ticker()
def parse_sues():
    pattern = r"Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)"
    for s in sues:
        num, p1, v1, p2, v2, p3, v3 = regex.search(pattern, s).groups()
        v1, v2, v3 = int(v1), int(v2), int(v3)
        yield {p1: v1, p2: v2, p3: v3}

def gt(a,b):
    return a>b

def lt(a,b):
    return a<b

def eq(a,b):
    return a==b

equations = {
    "children": eq,
    "cats": gt,
    "samoyeds": eq,
    "pomeranians": lt,
    "akitas": eq,
    "vizslas": eq,
    "goldfish": lt,
    "trees": gt,
    "cars": eq,
    "perfumes": eq,
}


def compare_sue(s):
    for key, value in s.items():
        if value != ticker_output[key]:
            if not equations[key](value, ticker_output[key]):
                return False
    return True

for i, s in enumerate(parse_sues()):
    if compare_sue(s):
        print (i+1)