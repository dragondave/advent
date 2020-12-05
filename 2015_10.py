# 107312 too low
# 469694 too high

def length_looksay(s,offset=0):
    first = s[offset]
    for i in range(len(s)-offset):
        if s[i+offset] != first:
            return [i, s[offset]]
    return [len(s)-offset, s[offset]]

def looksay(s):
    # print(s)
    w = []
    while s:
        l,v = length_looksay(s, 0)
        w.extend([l, v])
        s=s[l:]
    return ''.join([str(x) for x in w])

def looksay2(s):
    offset = 0
    w = []
    while len(s) > offset:
        try:
            l,v = length_looksay(s, offset)
        except:
            print (s, len(s), offset)
            raise
        w.extend([l, v])
        offset = offset+l
    return ''.join([str(x) for x in w])


real = '1113122113'
l = real
for i in range(50):
    l = looksay2(l)
    if i==39:
        assert len(l) == 360154
    if i==5:
        assert len(l) == 44

    print (i, len(l), l[:100])