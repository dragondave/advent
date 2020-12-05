import input
import json
import regex

# 176852 too high

sample = """[
    [1,2,3],
    {"a":2,"b":4},
    [[[3]]],
    {"a":{"b":4},"c":-1},
    {"a":[-1,1]},
    [-1,{"a":1}],
    [],
    {}
]"""

verify = 156366

j = input.input_raw(12,2015)
jj = json.loads(j)

# part 1
r = regex.findall(r'-?\d+', j)
print (sum([int(x) for x in r]))

# part 2
print ("--")

def jsonsum(item, red):
    count = 0
    if type(item) == int:
        count += item
    elif type(item) == str:
        pass
    elif type(item) == dict:
        for value in item.values():
            if value == "red" and not red:
                return 0
        for value in item.values():
            count += jsonsum(value, red)
    elif type(item) == list:
        for entry in item:
            count += jsonsum(entry, red)
    else:
        print (type(item))
        raise RuntimeError
    return count

print (jsonsum(jj, True))
print (jsonsum(jj, False))