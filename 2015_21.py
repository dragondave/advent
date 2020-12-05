# boss
hp=100
damage=8
armour=2

# me
hp =100

weapons = {4:8, 5:10, 6:25, 7:40, 8:74}
armour = {0:0, 1:13, 2:31, 3:53, 4:75, 5:102}
ring_dam = {0:0, 1:25, 2:25, 3:100}
ring_arm = {0:0, 1:20, 2:40, 3:80}

class Character(object):
    def __init__(self, hp, damage, armour):
        self.hp = hp
        self.damage = damage
        self.armour = armour

real_boss = Character(100, 8, 2)
samp_boss = Character(12, 7, 2)
samp_pc = Character(8, 5, 5)

def fight(pc, boss):
    pc_net = max(pc.damage - boss.armour, .0001)
    boss_net = max(boss.damage - pc.armour, .0001)
    boss_rounds = int(boss.hp / pc_net)
    pc_rounds = int(pc.hp / boss_net)
    #print (boss_rounds, pc_rounds)

    return pc_rounds >= boss_rounds # player wins ties

print (fight(samp_pc, samp_boss))

for dam in range(4,13+2):
    for arm in range(0,10+2):
        f = fight(Character(100, dam, arm), real_boss)
        if not f:
            print (dam, arm)