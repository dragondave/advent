sample = """
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
""".strip()

sample_bad = """
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
""".strip()

sample_good = """
pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
""".strip()

def v_byr(x):
    v = int(x)
    return v>=1920 and v<=2002

def v_iyr(x):
    v = int(x)
    return v>=2010 and v<=2020

def v_eyr(x):
    v = int(x)
    return v>=2020 and v<=2030

def v_hgt(x):
    if 'cm' in x:
        v = int(x[:-2])
        return v>=150 and v<=193
    elif 'in' in x:
        v = int(x[:-2])
        return v>=59 and v<=76

def v_hcl(x):
    if x[0]!='#': return False
    for i in range(1,7):
        if x[i] not in '0123456789abcdef':
            return False
    if len(x) != 7:
        return False
    return True

def v_ecl(x):
    return x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def v_pid(x):
    for i in x:
        if i not in '0123456789':
            return False
    if len(x) != 9:
        return False
    return True

def v_cid(x):
    return True


import input
import regex
data = input.input_raw(sample_good)
data = input.input_raw(4)
pports = data.split('\n\n')
pports = [p.replace("\n", " ") for p in pports]

mand_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid",]
mand_fields = {
    'byr': v_byr,
    'iyr': v_iyr,
    'eyr': v_eyr,
    'hgt': v_hgt,
    'hcl': v_hcl,
    'ecl': v_ecl,
    'pid': v_pid,
}

all_fields = list(mand_fields)
all_fields.append("cid")

def valid(pport):
    for field in mand_fields:
        if field+":" not in pport:
            return False
    return True

def valid_2(pport):
    if not valid(pport):
        return False
    for field, function in mand_fields.items():
        try:
            x = regex.search(r" {}:([^ ]+) ".format(field), " "+pport+" ").groups()
        except:
            print ("Did not find {} in {}".format(field, repr(pport)))
            return False
        if not function(x[0]):
            return False
    return True

c = 0
for pport in pports:
    if valid_2(pport):
        c += 1
print(c)


