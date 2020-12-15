# registers non-negative, a/b

sample = """inc a
jio a, +2
tpl a
inc a"""

import re
import input
from time import sleep

class State(object):
    def __init__(self):
        self.reg = {'a': 1, 'b': 0}
        self.pc = 0

    def ihlf(self, r, offset):
        self.reg[r] = self.reg[r] // 2
        self.pc += 1

    def itpl(self, r, offset):
        self.reg[r] = self.reg[r] * 3
        self.pc += 1

    def iinc(self, r, offset):
        self.reg[r] = self.reg[r] + 1
        self.pc += 1

    def ijmp(self, r, offset):
        #if offset == "+23":
        #    print ("FAKE")
        #    offset = "24"
        self.pc += int(offset)

    def ijie(self, r, offset):
        if self.reg[r] % 2 == 0:
            self.pc += int(offset)
        else:
            self.pc += 1
    
    def ijio(self, r, offset):
        if self.reg[r] == 1:
            self.pc += int(offset)
        else:
            self.pc += 1

    instructions = {
        "hlf": ihlf,
        "tpl": itpl,
        "inc": iinc,
        "jmp": ijmp,
        "jie": ijie,
        "jio": ijio,
    }

    def parse(self, s):
        instruction, register, offset = re.search("(...) ([ab])?(?:, )?(.*)?",s).groups()
        self.instructions[instruction](self, register, offset)

    def run(self, script):
        while self.pc<len(script):
            print ("PC: {} {}".format(self.pc, script[self.pc]), end=" ... ")
            self.parse(script[self.pc])
            print ("A: {}, B: {}, PC: {}".format(self.reg['a'], self.reg['b'], self.pc))
            #sleep(.2)


#data = input.input(sample)
data = input.input(23, 2015)
machine = State()

machine.run(data)



