import input
import numpy as np
sample = """
F10
N3
F7
R90
F11
""".strip()

data = input.input(sample)
data = input.input(12)

pos = np.array([10,1]) # waypoint offset from ship
ship_true = np.array([0,0])

def absolute(x,y):
    global pos
    pos = pos + np.array([x, y])

def n(x):
    absolute(0, x)

def s(x):
    absolute(0, -x)

def e(x):
    absolute(x, 0)

def w(x):
    absolute(-x, 0)

def f(d):
    global ship_true
    ship_true = ship_true + d*pos

def l(d):
    global pos
    turns = d//90
    for i in range(turns):
        pos = np.array([-pos[1], pos[0]])

def r(d):
    global pos
    turns = d//90
    for i in range(turns):
        pos = np.array([pos[1], -pos[0]])


"""
def f(d):
    x, y = np.array([d, d]).transpose() * np.array(facing)
    absolute(x,y)


def l(x):
    global facing
    table = {
        (1,0): np.array([0,1]),  # e->n
        (0,1): np.array([-1,0]), # n->w
        (-1,0): np.array([0,-1]),# w->s
        (0,-1): np.array([1,0]),  # s->e
        
    }
    turns = x//90
    assert turns*90 == x
    for i in range(turns):
        facing = table[tuple(facing)]


def r(x):
    global facing
    table = {
        (1,0): np.array([0,-1]),  # e->s
        (0,-1): np.array([-1,0]), # s->w
        (-1,0): np.array([0,1]),# w->n
        (0,1): np.array([1,0]),  # n->e
        
    }
    turns = x//90
    assert turns*90 == x
    for i in range(turns):
        facing = table[tuple(facing)]
"""
def parse(me):
    functions = {
        "f": f,
        "n": n,
        "s": s,
        "e": e,
        "w": w,
        "l": l,
        "r": r,
    }
    c = me[0]
    x = int(me[1:])
    functions[c.lower()](x)

def do():
    global ship_true
    global pos
    parse("F10")
    parse("N3")
    parse("F7")
    parse("R90")
    parse("F11")
    assert list(ship_true)==[214,-72]
    assert list(pos) == [4,-10]
    pos = np.array([10,1]) # waypoint offset from ship
    ship_true = np.array([0,0])
    parse("R90")
    parse("R90")
    parse("R90")
    parse("R90")
    assert list(pos) == [10, 1]
    pos = np.array([10,1]) # waypoint offset from ship
    ship_true = np.array([0,0])
    parse("L90")
    parse("L90")
    parse("L90")
    parse("L90")
    assert list(pos) == [10, 1]
    pos = np.array([10,1]) # waypoint offset from ship
    ship_true = np.array([0,0])
    parse("L90")
    parse("L270")
    assert list(pos) == [10, 1]
    pos = np.array([10,1]) # waypoint offset from ship
    ship_true = np.array([0,0])
    parse("L180")
    parse("R180")
    assert list(pos) == [10, 1]
    pos = np.array([10,1]) # waypoint offset from ship
    ship_true = np.array([0,0])
    parse("R720")
    assert list(pos) == [10, 1]
    pos = np.array([10,1]) # waypoint offset from ship
    ship_true = np.array([0,0])
    parse("N3")
    assert list(pos) == [10, 4]
    parse("S3")
    assert list(pos) == [10, 1]
    parse("E3")
    assert list(pos) == [13, 1]
    parse("W3")
    assert list(pos) == [10, 1]
    # wrong value delib
    ship_true = np.array([0,0])
    pos = np.array([0,0])
    parse("F10")
    assert list(pos) == [0,0]
    pos = np.array([10,1]) # waypoint offset from ship
    ship_true = np.array([0,0])
    parse("F10")
    assert list(ship_true) == [100,10]
    assert list(pos) == [10,1]
    
    

    
    


do()
pos = np.array([10,1]) # waypoint offset from ship
ship_true = np.array([0,0])


def do2():
    print(pos, ship_true)
    parse("R90")
    print(pos, ship_true)
    parse("R90")
    print(pos, ship_true)
    parse("R90")
    print(pos, ship_true)
    parse("R90")
    print(pos, ship_true)
    parse("R360")
    print(pos, ship_true)
    #assert tuple(pos)==(17, -8), tuple(pos)
print(pos, ship_true)
for i in data:
    print (i)
    parse(i)
    print(pos, ship_true)
print (ship_true)

# not 85