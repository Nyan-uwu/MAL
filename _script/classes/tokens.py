import sys

sys.path.insert(1, '../functions')
import response

class Master:
    name = None
    value = None
    params = []
    def __init__(self, _dict):
        if "name" not in _dict:
            return response.create(301, "Invalid Token Dictionary: Missing key 'name'")
        else:
            self.name = _dict["name"]
            
        if _dict["name"] == "int" or _dict["name"] == "memloc" or _dict["name"] == "jmp":
            if "value" not in _dict:
                return response.create(301, "Invalid Token Dictionary: Missing key 'value'")
            else:
                self.value = _dict["value"]

        if "params" in _dict:
            self.params = _dict["params"]

    def __str__(self):
        return "{}:{}".format(self.name, self.params)

    def run(self, memory):
        return memory

class Mov(Master):
    def __str__(self):
        return "{}\nValue: {}\nLocation: {}".format(self.name, self.params[0], self.params[1])

    def run(self, memory):
        if self.params[0].name == "int":
            memory.write(self.params[0].value, self.params[1].value)
        elif self.params[0].name == "memloc":
            memory.write(memory.read(self.params[0].value), self.params[1].value)
            
        return memory

class Int(Master):
    def __str__(self):
        return "Int: {}".format(self.value)

class MemLoc(Master):
    def __str__(self):
        return "Memory Location: {}".format(self.value)

class Label(Master):
    def __str__(self):
        return "Label: {}".format(self.value)

class Jump(Master):
    def __str__(self):
        return "Jump: {}".format(self.value)
    def run(self, tokenFile):
        for couple in tokenFile.labels:
            if couple[0] == self.value:
                return couple[1]
        res = response.create("701", "Label Does Not Exist: {}".format(self.value))
        raise Exception(res["message"])

class Test(Master):
    def __str__(self):
        return "Test: {}".format(self.name)
    def run(self, memory):
        val1 = None
        val2 = None
        if self.params[0].name == "memloc":
            val1 = memory.read(self.params[0].value)
        else:
            val1 = self.params[0].value
        if self.params[1].name == "memloc":
            val2 = memory.read(self.params[1].value)
        else:
            val2 = self.params[1].value

        print("params")
        for p in self.params:
            print(p)
        
        if self.name == "teq":
            print("TEQ {} == {}".format(val1, val2))
            return val1 == val2
        elif self.name == "tgt":
            return val1 > val2
        elif self.name == "tgte":
            return val1 >= val2
        elif self.name == "tlt":
            return val1 < val2
        elif self.name == "tlte":
            return val1 <= val2

class IfTrueBlockStart(Master):
    def __str__(self):
        return "True Block (Start): {}".format(self.value)

class IfTrueBlockEnd(Master):
    def __str__(self):
        return "True Block (End): {}".format(self.value)
        
class IfFalseBlockStart(Master):
    def __str__(self):
        return "False Block (Start): {}".format(self.value)

class IfFalseBlockEnd(Master):
    def __str__(self):
        return "False Block (End): {}".format(self.value)


def findRelatedStartBlock_True(tokenArr, startPos):
    counter = 0
    pos = startPos-1
    while pos >= 0:
        if tokenArr[pos].name == "truestart" and counter == 0:
            tokenArr[pos].value = startPos
            break
        elif tokenArr[pos].name == "truestart" and not counter == 0:
            counter -= 1
        elif tokenArr[pos].name == "trueend":
            counter += 1

        pos -= 1

def findRelatedStartBlock_False(tokenArr, startPos):
    counter = 0
    pos = startPos-1
    while pos >= 0:
        if tokenArr[pos].name == "falsestart" and counter == 0:
            tokenArr[pos].value = startPos
            break
        elif tokenArr[pos].name == "falsestart" and not counter == 0:
            counter -= 1
        elif tokenArr[pos].name == "falseend":
            counter += 1

        pos -= 1