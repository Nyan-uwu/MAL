import sys

sys.path.insert(1, '../functions')
import response

class Master:
    name = None
    def __init__(self, _dict):
        if "name" not in _dict:
            return response.create(301, "Invalid Token Dictionary: Missing key 'name'")


class Mov(Master):
    def __init__(self, _dict)    pass:
        super(_dict)