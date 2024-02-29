class Class():
    def __init__(self,name,level,supers) -> None:
        self.level = level
        self.name = name
        self.methods = []
        self.attributes = []
        self.supers = supers
        self.description = 'N/A'

    def __str__(self) -> str:
        final = {
            'name':self.name,
            'methods':self.methods,
            'attributes': self.attributes,
            'level': self.level,
            'description' : self.description
        }
        return f'{final}'
    def __repr__(self) -> str:
        final = {
            'name':self.name,
            'methods':self.methods,
            'attributes': self.attributes,
            'level': self.level,
            'description' : self.description
        }
        return f'{final}'
    def __eq__(self, other) -> bool:
        return self.name == other.name 
                
    
        
class Function():
    def __init__(self,name,level,parameters) -> None:
        self.level = level
        self.name = name
        self.parameters = parameters
        self.description = 'N/A'
    def __repr__(self) -> str:
        final = {
            'name':self.name,
            'parameters': self.parameters,
            'level': self.level,
            'description' : self.description
        }
        return f'{final}'
    def __eq__(self, other) -> bool:
        return self.name == other.name 
                

    

class Variable():
    def __init__(self,name,value,kind,level) -> None:
        self.level = level
        self.name = name
        self.value = value
        self.kind = kind
        self.description = 'N/A'
    def __repr__(self) -> str:
        final = {
            'name':self.name,
            'Initial value': self.value,
            'level': self.level,
            'description' : self.description
        }
        return f'{final}' 
    def __eq__(self, other) -> bool:
        return self.name == other.name 

    