sample = """
abc

a
b
c

ab
ac

a
a
a
a

b
""".strip()

sample_0 = """
abcx
abcy
abcz
"""

alphabet = "abcdefghijklmnopqrstuvwxyz"
assert len(alphabet)==26
import input
data = input.input_raw(6)
groups = data.split("\n\n")

# part 1
s=0
for g in groups:
    yes = set(g.replace("\n", ""))
    s=s+len(yes)
print(s)

su=0
for g in groups:
    s = 0
    letters = []
    people = g.strip().split("\n")
    for l in alphabet:
        if g.count(l) == len(people):
            s=s+1
            letters.append(l)
    print ([''.join(sorted(x)) for x in people])
    print (s, letters)
    
    su=su+s

print(su)
# 3346 too low