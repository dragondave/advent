from copy import deepcopy
class State(object):
    def __init__(self):
        self.b_dmg = 8
        self.shield = 0
        self.poison = 0
        self.recharge = 0

class Win(Exception):
    pass

def debug(s):
    pass
    #print (s)

sample_1 = State()
sample_1.pc_hp = 10
sample_1.b_hp = 13
sample_1.mana = 250

sample_2 = State()
sample_2.pc_hp = 10
sample_2.b_hp = 14
sample_2.mana = 250

real = State()
real.pc_hp = 50
real.pc_mana = 500
real.b_hp = 55

def fight(spell, s):
    def apply_status():
        if s.shield:
            s.shield -= 1
            if not s.shield:
                debug ("Shield wears off.")

        if s.poison:
            s.poison -= 1
            s.b_hp -= 3
            debug ("Poison deals 3 damage; its timer is now {}".format(s.poison))
            if not s.poison:
                debug ("Poison wears off.")

        if s.recharge:
            s.recharge -= 1
            s.mana += 101
            debug ("Recharge provides 101 mana; its timer is now {}".format(s.recharge))
            if not s.recharge:
                debug ("Recharge wears off.")
    
    s = deepcopy(s)

    debug('-- Player turn --')
    debug('- Player has {} hitpoints, {} armor, {} mana -'.format(s.pc_hp, bool(s.shield)*7, s.mana))
    debug('- Boss has {} hitpoints'.format(s.b_hp))
    apply_status()

    if spell == "poison":
        assert not s.poison
        s.poison = 6
        s.mana -= 173
        debug("Player casts Poison.")

    if spell == "recharge":
        assert not s.recharge
        s.recharge = 5
        s.mana -= 229
        debug("Player casts Recharge.")

    if spell == "shield":
        assert not s.shield
        s.shield = 6
        s.mana -= 113
        debug("Player casts Shield, increasing armor by 7.")

    if spell == "drain":
        s.mana -= 73
        s.b_hp -= 2
        s.pc_hp += 2
        debug("Player casts Drain, dealing 2 damage and healing 2 hit points.")

    if spell == "missile":
        s.mana -= 53
        s.b_hp -= 4
        debug("Player casts Magic Missile, dealing 4 damage")

    assert s.mana >=0, s.mana
    if s.b_hp <= 0:
        debug("This kills the boss, and the player wins.")
        raise Win()
    
    debug("")
    debug("-- Boss turn --")
    debug('- Player has {} hitpoints, {} armor, {} mana -'.format(s.pc_hp, bool(s.shield)*7, s.mana))
    debug('- Boss has {} hitpoints'.format(s.b_hp))
    apply_status()
    if s.b_hp <= 0:
        debug("This kills the boss, and the player wins.")
        raise Win()

    if s.shield:
        debug("Boss attacks for 8 - 7 = 1 damage!")
        s.pc_hp -= 1
    else:
        debug("Boss attacks for 8 damage.")
        s.pc_hp -= 8
    debug("")
    assert s.pc_hp > 0, s.pc_hp
    return s

"""
f=sample_1
f=fight("poison", f)
try:
    f=fight("missile", f)
except Win:
    pass
else:
    raise RuntimeError

f=sample_2
f=fight("recharge", f)
f=fight("shield", f)
f=fight("drain", f)
f=fight("poison", f)
try:
    f=fight("missile", f)
except Win:
    pass
else:
    raise RuntimeError
"""

spells = {
    "missile":53,
    "drain":73,
    "shield":113,
    "poison":173,
    "recharge":229
}

def run_fight(spells, state):
    f = deepcopy(state)
    for spell in spells:
        try:
            f = fight(spell, f)
        except AssertionError:
            return False
        except Win:
            return True
    return 0

#print (run_fight(["recharge", "shield", "drain", "poison", "missile"], sample_2))

from itertools import combinations_with_replacement as combo

def mana(spelllist):
    m = 0
    for spell in spelllist:
        m += spells[spell]
    return m

depth = 0
while True:
    depth = depth + 1
    spelllists = combo(spells, depth)
    for spelllist in spelllists:
        victory = run_fight(spells, sample_2)
        if victory == False:
            print ("BAD")
            exit()

    


    
        


    


