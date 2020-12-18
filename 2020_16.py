sample = """
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
""".strip()

sample_2 = """
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
""".strip()

import input
sample = input.input(sample_2)

real = input.input(16)

data = real
nearby_placeholder = data.index("nearby tickets:")
tickets = [[int(y) for y in x.split(',')] for x in data[nearby_placeholder+1:]]


your_placeholder = data.index("your ticket:")
your_ticket = [int(y) for y in data[your_placeholder+1].split(',') ]
class_end = data.index("")
raw_classes = data[:class_end]
classes = {}
for cat in raw_classes:
    name, _, valid_text = cat.partition(": ")
    pre, _, post = valid_text.partition(" or ")
    a, _, b = pre.partition("-")
    c, _, d = post.partition("-")
    classes[name]= [int(a), int(b), int(c), int(d)]

count = 0
def is_ticket_valid(ticket):
    for value in ticket:
        valid = False
        for name in classes:
            a,b,c,d = classes[name]
            if (value >= a and value <= b) or (value >=c and value <= d):
                valid=True
        if not valid:
            return False
    return True

valid_tickets = [x for x in tickets if is_ticket_valid(x)]
valid_options = {}
print(valid_tickets)
for cat in classes:
    a,b,c,d = classes[cat]
    for column in range(len(valid_tickets[0])):
        valid = True
        for ticket in valid_tickets:
            value = ticket[column]
            if (value >= a and value <= b) or (value >=c and value <= d):
                pass
            else:
                valid = False
                break
        if valid:
            print ("{} could be column {}".format(cat, column))
            if column not in valid_options:
                valid_options[column] = []
            valid_options[column].append(cat)

print (valid_options)

while True:
    for column, options in valid_options.items():
        if len(options) == 1:
            choice = options[0]
            print (choice, column)
            break
    del valid_options[column]
    for column, options in valid_options.items():
        valid_options[column].remove(choice)
        



            


            
    
            

    
# classes, your_ticket, tickets
# 137984  too low