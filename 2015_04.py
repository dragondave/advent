key = 'ckczppom'
sample = 'abcdef'

import hashlib

i=0
while True:
    i=i+1
    r = hashlib.md5(key.encode('utf-8')+str(i).encode('utf-8')).hexdigest()
    if r[:6] == '000000':
        print (i)
        break
    if i % 1000 == 0:
        print (i)