sample = "0,3,6"
real = "16,11,15,0,1,7"
klange = "15,5,1,4,7,0"
import input
from collections import Counter
from time import time
t = time()

data = [int(x) for x in klange.split(",")]
print(data)

historic = Counter({x:i+1 for i, x in enumerate(data[:-1])})
historic = dict(historic)
turn = len(historic)
last = data[-1]

while turn < 30000000:
    turn = turn + 1
    if last in historic:
        age = turn - historic[last]
    else:
        age = 0
    historic[last] = turn
    if turn%1000000 == 0: print ("Turn {}: {} has age {}".format(turn, last, age))
    #print (historic)
    last = age
print (time()-t)
