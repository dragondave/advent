import input
import ast

sample = r"""
""
"abc"
"aaa\"aaa"
"\x27"
"""

score = 0
for x in input.input(8, 2015):
    a = ast.literal_eval(x)
    score += (len(x) - len(a))
    
print(score)
    
score = 0
for x in input.input(8, 2015):
    # .. -> ".." +2
    # " > \"  +1 
    # \ > \\  +1

    bonus = 2 + x.count('"') + x.count('\\')
    score += bonus
    print (x, bonus, len(x), len(x)+bonus)

print (score)
