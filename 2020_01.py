import input

sample_raw = """
1721
979
366
299
675
1456
"""
sample = input.input_int(sample_raw)


real = input.input_int(1)
data = real

print (data)

def part_1():
    for i in data:
        if 2020-i in data:
            print ((2020-i) * i)

def part_2():
    for i in data:
        for j in data:
            if 2020-i-j in data:
                print ((2020-i-j)*i*j)

part_1()
part_2()