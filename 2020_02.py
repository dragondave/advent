import input
import regex

real = input.input(2, 2020)
sample = input.input("""1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc""")

def parse(s):
    lo, hi, char, pwd = regex.search(r"(\d+)-(\d+) (\w): (.*)", s).groups()
    lo = int(lo)
    hi = int(hi)
    # part 1
    # return letters >= lo and letters <= hi
    return (pwd[lo-1] == char) + (pwd[hi-1] == char) == 1
    

count = 0
for pwd in real:
    if parse(pwd):
        count +=1
    print (parse(pwd))
print (count)

