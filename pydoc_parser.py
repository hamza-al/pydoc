import re
#dd Class representing the parser

class Parser():
    def __init__(self,file_name) :
        self.file = open(file_name,"r")
        self.file = self.file.read()
    def find_level(self,line):
        level = 0
        space_count = 0
        for i in line:
            if i == '\t':
                level += 1
            elif i == ' ':
                space_count +=1
                if space_count == 4:
                    level +=1
                    space_count = 0
            else:
                break
        return level
    def parse(self):
        i = 1
        for line in self.file.split('\n'):
            funcPattern = re.compile('\s*def\s*[a-zA-Z_]+\s*\(\s*(([a-zA-Z_]*\s*,)*\s*)*[a-zA-Z_]*\s*\)\s*:\s*')
            classPattern =  re.compile('\s*class\s*[a-zA-Z_]+\s*\(\s*(([a-zA-Z]*\s*,)*\s*)*[a-zA-Z]*\s*\)\s*:\s*')
            varPattern =  re.compile('\s*[a-zA-Z_]+\s*=\s*.+\s* ')
            if bool(re.fullmatch(funcPattern,line)):
                print(f"line {i}: func")
            elif bool(re.fullmatch(classPattern,line)):
                print(f"line {i}: class")
            elif bool(re.fullmatch(varPattern,line)):
                print(f"line {i}: var")
            i+=1
    def makeTree(self):
        tree  = {
            'classes':[],
            'functions':[],
            'variables': [],
        }
        currLevel = 0
        for i in range(len(self.file.split('\n'))):
            level = self.find_level(self.file.split('\n')[i])
        

    def show(self):
        print(self.file)

x = Parser('pydoc_parser.py') 
x.parse()
