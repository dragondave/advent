import input

real = input.input(2, 2015)

def box(l, w, h):
    return 2*l*w + 2*w*h + 2*h*l + smallest_side(l, w, h)

def ribbon(l, w, h):
    return smallest_peri(l, w, h) + l*w*h


def smallest_peri(l, w, h):
    a, b, c = sorted([l, w, h])
    return a+b+a+b
    

def smallest_side(l, w, h):
    a, b, c = sorted([l, w, h])
    return a*b

assert box(2,3,4) == 58
assert box(1,1,10) == 43

c = 0
for i in real:
    str_dims = i.split('x')
    dims = [int(x) for x in str_dims]
    c = c + box(dims[0], dims[1], dims[2])

print (c)
r=0

assert ribbon(2,3,4) == 34
assert ribbon(1,1,10) == 14
for i in real:
    str_dims = i.split('x')
    dims = [int(x) for x in str_dims]
    r = r + ribbon(dims[0], dims[1], dims[2])

print (r)
