import input
floor = 0
# ( = up
# ) = down

real = input.input_raw(1, 2015)

samples = {
    "(())": 0,
    "()()": 0,
    "(((": 3,
    "(()(()(": 3,
    "))(((((": 3,
    "())": -1,
    "))(": -1,
    ")))": -3,
    ")())())": -3,
}

samples_2 = {
    ")": 1,
    "()())": 5,
}

def lift(s):
    return s.count("(") - s.count(")")

def part_1():
    for k, v in samples.items():
        assert lift(k) == v
    print (lift(real))

def basement(s):
    c = 0
    for i, x in enumerate(s):
        if x == "(":
            c = c + 1
        if x == ")":
            c = c - 1
            if c < 0: return i+1

def part_2():
    for k, v in samples_2.items():
        assert basement(k) == v
    print (basement(real))

part_2()
