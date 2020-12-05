# not sure what this program is doing at the end, but it seems to give the right answer...

import input
import regex
real = input.input(19,2015)
sample = input.input("""
H => HO
H => OH
O => HH

HOH
""")


irreducible = set()
raw = real
molecule = raw[-1]
trimmed = raw[:-2]
replacements = [regex.search(r'(\w+) => (\w+)', s).groups() for s in trimmed]
score = 9999

def simplify(molecule, depth=0):
    global score
    depth = depth + 1
    new_molecules = set()
    for replacement in replacements:
        targets = regex.finditer(replacement[1], molecule)
        for target in targets:
            prefix = molecule[:target.span()[0]]
            postfix = molecule[target.span()[1]:]
            new_molecule = prefix + replacement[0] + postfix
            if new_molecule not in irreducible:
                new_molecules.add(new_molecule)
    if not new_molecules:
        irreducible.add(molecule)
    for new_molecule in new_molecules:
        if new_molecule == 'e':
            if score > depth:
                print (score, depth)
                score = depth
                print (score)
            irreducible.add(molecule)
            print ("made {} irreducible".format(molecule))
            
        else:
            simplify(new_molecule, depth)

simplify(molecule)

# part 1
"""
new_molecules = set()

for replacement in replacements:
    targets = regex.finditer(replacement[0], molecule)
    for target in targets:
        prefix = molecule[:target.span()[0]]
        postfix = molecule[target.span()[1]:]
        new_molecules.add( prefix + replacement[1] + postfix )

print (len(new_molecules))
"""