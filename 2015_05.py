import regex
import input

data = input.input(5, 2015)

def is_nice(s):
    return nice_1(s) and nice_2(s) and nice_3(s)

def nice_1(s):
    vowels = 0
    for v in "aeiou":
        vowels += s.count(v)
    return vowels >= 3

def nice_2(s):
    return bool(regex.search(r'(.)\1', s))

def nice_3(s):
    for naughty in ['ab', 'cd', 'pq', 'xy']:
        if naughty in s:
            return False
    return True

assert nice_1('ugknbfddgicrmopn')
assert nice_2('ugknbfddgicrmopn')
assert nice_3('ugknbfddgicrmopn')
assert is_nice('ugknbfddgicrmopn')

assert is_nice('aaa')
assert not nice_2('jchzalrnumimnmhp')
assert not nice_3('haegwjzuvuyypxyu')
assert not nice_1('dvszwmarrgswjxmb')

c=0
for d in data:
    if is_nice(d):
        c=c+1
print(c)

def nice_4(s):
    return bool(regex.search(r'(..).*\1', s))

def nice_5(s):
    return bool(regex.search(r'(.).\1', s))

def is_nicer(s):
    return nice_4(s) and nice_5(s)

assert is_nicer('qjhvhtzxzqqjkmpb')
assert is_nicer('xxyxx')
assert not nice_5('uurcxstgmygtbstg')
assert not nice_4('ieodomkazucvgmuy')

c=0
for d in data:
    if is_nicer(d):
        c=c+1
print(c)