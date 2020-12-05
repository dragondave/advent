# wire 0..65535
import input
import regex

sample = """
123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
"""

data = {}

def value(s):
    try:
        return int(s)
    except:
        return data[s]


def OP_ASSIGN(a,b,out):
    data[out] = value(a)
def OP_AND(a,b,out):
    data[out] = value(a) & value(b)
def OP_OR(a,b, out):
    data[out] = value(a) | value(b)
def OP_LSHIFT(a,b, out):
    data[out] = value(a) << value(b)
def OP_RSHIFT(a,b, out):
    data[out] = value(a) >> value(b)
def OP_NOT(a,b, out):
    data[out] = value(a) ^ 65535

commands = {
    r"^([a-z0-9]+)() -> ([a-z]+)$": OP_ASSIGN,
    r"^([a-z0-9]+) AND ([a-z0-9]+) -> ([a-z]+)$": OP_AND,
    r"^([a-z0-9]+) OR ([a-z0-9]+) -> ([a-z]+)$": OP_OR,
    r"^([a-z0-9]+) LSHIFT (\d+) -> ([a-z]+)$": OP_LSHIFT,
    r"^([a-z0-9]+) RSHIFT (\d+) -> ([a-z]+)$": OP_RSHIFT,
    r"^NOT ([a-z0-9]+)() -> ([a-z0-9]+)$": OP_NOT,
}
    
def parse(s):
    for command, f in commands.items():
        search = regex.search(command, s)
        if search:
            return f, search.groups()
    print (s)
    raise RuntimeError

while True:
    for x in input.input(7, 2015):
        # print (x)
        f, params = parse(x)
        # print (f, params)
        try:
            f(*params)
            ## part 2: data['b'] = 16076
        except KeyError:
            # print("Skipping ", f, params)
            continue
        
    try:
        print (data['a'])
        exit()
    except KeyError:
        pass