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
            
        if _dict["name"] == "int" or _dict["name"] == "memloc":
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