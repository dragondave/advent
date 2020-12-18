import input
import regex
import math
sample = """
1 + 2 * 3 + 4 * 5 + 6
1 + (2 * 3) + (4 * (5 + 6))
2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
""".strip()

data = input.input(sample)
data = input.input(18)

def unadd(math):
    math = math.replace(" ", "")
    while True:
        s = regex.search(r"(\d+\+\d+)", math)
        if not s:
            break
        pre, post = s.span()
        new_math = math[pre:post]
        value = calc(new_math)
        math = math[:pre]+str(value)+math[post:]
    return math

def unbracket(math):
    s = regex.search(r"(\([^)(]+\))", math)
    if not s:
        return math
    pre, post = s.span()
    new_math = math[pre+1:post-1]
    assert "(" not in new_math
    value = calc(new_math)
    
    math = math[:pre]+str(value)+math[post:]
    
    return math

def tokenise(math):
    tokens = []
    num = []
    for char in math:
        if char == " ":
            continue
        if char in "0123456789":
            num.append(char)
        else:
            if num:
                tokens.append(int(''.join(num)))
                num = []
            tokens.append(char)
    if num:
        tokens.append(int(''.join(num)))
    return tokens

f = {'+': int.__add__,
     '*': int.__mul__}

def calc(math):
    num = None
    op = None
    tokens = tokenise(math)
    for token in tokens:
        if type(token) == str:
            op = f[token]
        else:
            if num is None:
                num = token
            else:
                num = op(num, token)
                op = None
    if op:
        num = op(num, token)
    return num

total = 0
for math in data[:]:
    un = math
    while True:
        #print(un)
        old = None
        while old != un:
            un = unadd(un)
            old = un
        #    print("unadd", un)
        
        
        un = unbracket(un)
        #print("unbracket", un)
        
        
        if ")" not in un and "+" not in un:
            break

        
    
    
    calculation = calc(un)
    print(calculation)
    total = total + calculation
    #print(calc(un))
print(total)
