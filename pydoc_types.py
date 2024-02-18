class Class():
    def __init__(self,name) -> None:
        self.name = name
        self.methods = []
        self.attributes = []

class Function():
    def __init__(self,name) -> None:
        self.name = name
        self.parameters = []

class Variable():
    def __init__(self,name,value,kind) -> None:
        self.name = name
        self.value = value
        self.kind = kind