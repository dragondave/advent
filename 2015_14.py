import regex
import input

# 1092: too low

reindeer = {}
class Reindeer(object):
    def __init__(self, s):
        pattern = r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds\."
        print(s)
        self.str=s
        self.name, speed, duration, rest = regex.search(pattern, s).groups()
        self.speed = int(speed)
        self.duration = int(duration)
        self.rest = int(rest)
        self.cycle = self.duration + self.rest
        self.go_seconds = 0
        self.rest_seconds = 0
        reindeer[self.name] = self

    def pos(self, tt):
        t = tt
        p = 0
        while t >= self.cycle:
            p += self.speed * self.duration
            t = t - self.cycle
        p += self.speed * min(t, self.duration)
        return p

    def __repr__(self):
        return self.str

real = input.input(14, 2015)
sample = input.input("""
Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
""")

all_reindeer_list = [Reindeer(x) for x in real]

#fake_deer = Reindeer("Bob can fly 2 km/s for 5 seconds, but then must rest for 10 seconds.")
#for x in range(35):
#
#     print (x, fake_deer.pos(x))

print (reindeer)
from collections import Counter
scores = Counter()


def max_reindeer(t):
    data = Counter()
    for r in reindeer:
        data[r] = reindeer[r].pos(t)
    winscore = max(data.values())
    for r in data:
        if data[r] == winscore:
            scores[r] += 1
    
for t in range(1, 2503+1):
#for t in range(0, 1001):
    max_reindeer(t)

# more than 648
print (scores)
    



