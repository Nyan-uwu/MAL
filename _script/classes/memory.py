import sys

class Memory:
    mem = [0] * 100
    memSize = len(mem)

    def read(self, location):
        return self.mem[location]

    def write(self, value, location):
        self.mem[location] = value