# just did it by inspection
# this code is guff
# 
def incr(s):
    last = s[-1]
    if ord(last) >= ord('z'):
        plusone = chr(ord(last)+1)
        word = s[:-1]+plusone+"aaaaaaaaa"
        return word[:8]
    else:
        return incr(s[:-1])

    

def valid_1(s):
    for i in range(len(s)-2):
        if ord(s[i]) + 1 == ord(s[i+1]) and ord(s[i+1]) +1 == ord(s[i+2]):
            return True
    return False

def valid_2(s):
    forb = "iol"
    for f in forb:
        if f in s:
            return False
    return True

def valid_3(s):
    pass

print (valid_1("abzzef"))
