#\Title Pydoc_parse
# \Date 
# \Author Hamza Al Sorkhy, Mohammad Sumbul

# reqs
import re
from pydoc_types import *
#c Class describing a python file parser 
class Parser():
    def __init__(self,file_name) :
        self.file_name = file_name
        self.file = open(file_name,"r")
        self.file = self.file.read()
        self.trial = 'x'
    def find_level(self,line):
        level = 1
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
    #f Parses each line to find type
    def parseComments(self,line):
        titlePattern = re.compile('\s*#\s*\\\s*(title|Title)\s*.*\s*')
        authPattern = re.compile('\s*#\s*\\\s*(author|Author)\s* .*\s*')
        datePattern = re.compile('\s*#\s*\\\s*(date|Date)\s*')
        descPattern = re.compile('')
        if bool(re.fullmatch(titlePattern,line)):
            return 0
        elif bool(re.fullmatch(authPattern,line)):
            return 1
        elif bool(re.fullmatch(datePattern,line)):
            return 2

        pass
    def parse(self,line):
        funcPattern = re.compile('\s*def\s*[a-zA-Z_]+\s*\(\s*(([a-zA-Z_]*\s*,)*\s*)*[a-zA-Z_]*\s*\)\s*:\s*')
        classPattern =  re.compile('\s*class\s*[a-zA-Z_]+\s*\(\s*(([a-zA-Z]*\s*,)*\s*)*[a-zA-Z]*\s*\)\s*:\s*')
        varPattern =  re.compile('\s*[a-zA-Z_]+\s*=\s*.+\s* ')
        attrPattern = re.compile('\s*self\.\s*[a-zA-Z_]+\s*=\s*.+\s*')
        if bool(re.fullmatch(classPattern,line)):
            return 0
        elif bool(re.fullmatch(funcPattern,line)):
            return 1
        elif bool(re.fullmatch(varPattern,line)):
            return 2
        elif bool(re.fullmatch(attrPattern,line)):
            return 3
    def makeTree(self):
        tree  = {
            'classes': [],
            'functions':[],
            'variables': [],
            'title':'',
            'author':'',
            'date':'',

        }
        lines = self.file.split('\n')
        for i in range(len(lines)):
            if self.find_level(lines[i]) <= 2:
                kind = self.parse(lines[i])
                if kind == None:
                    if self.parseComments(lines[i]) == 0:
                        title =  lines[i].split(' ')
                        title = [j for j in title if j != '' ]
                        print(title)
                        tree['title'] = ''
                if kind == 0:
                    parts = lines[i].split(' ')
                    parts = [j for j in parts if j != '' ]
                    dec = ''.join(parts[1:])
                    name = dec[:dec.index('(')]
                    supers = dec[dec.index('(')+1:dec.index(')')].split(',')
                    supers = [j for j in supers if j != '']
                    cls = Class(name,self.find_level(lines[i]),supers)
                    if cls not in tree['classes']:
                        tree['classes'].append(cls)
                elif kind == 1:
                    if tree['classes'] == []:
                        isMethod = False
                    else:
                        isMethod = self.find_level(lines[i]) > tree['classes'][-1].level
                    parts = lines[i].split(' ')
                    parts = [j for j in parts if j != '' ]
                    dec = ''.join(parts[1:])
                    name = dec[:dec.index('(')]
                    params = dec[dec.index('(')+1:dec.index(')')].split(',')
                    params = [j for j in params if j != '']
                    func = Function(name,self.find_level(lines[i]),params)
                    if isMethod:
                        if func not in tree['classes'][-1].methods:
                            tree['classes'][-1].methods.append(func)
                    else:
                        if func not in tree['functions']:
                            tree['functions'].append(func)
                elif kind == 2:
                    if tree['classes'] == []:
                        isAttr = False
                    else:
                        isAttr = self.find_level(lines[i]) > tree['classes'][-1].level
                    parts = lines[i].split('=')
                    parts[0] = parts[0].replace(' ','')
                    name = parts[0]
                    parts[1] = parts[1].replace(' ','')
                    value = parts[1]
                    var = Variable(name,value,'',self.find_level(lines[i]))
                    if isAttr:
                        if var not in tree['classes'][-1].attributes:
                            tree['classes'][-1].attributes.append(var) 
                    else:
                        if var not in tree['variables']:
                            tree['variables'].append(var)
            elif self.find_level(lines[i]) == 3:
                kind = self.parse(lines[i])
                
                if kind == 3:
                        parts = lines[i].split('=')
                        parts[0] = parts[0].replace(' ','')
                        name = parts[0]
                        
                        parts[1] = parts[1].replace(' ','')
                        value = parts[1]
                        if tree['classes'] != [] and tree['classes'][-1].methods[-1].name == '__init__':
                            var = Variable(name,value,'',self.find_level(lines[i]))
                            if var not in tree['classes'][-1].attributes:
                                tree['classes'][-1].attributes.append(Variable(name,value,'',self.find_level(lines[i]))) 

        return tree
    def show(self):
        print(self.file)

    def funcMD(self,func:Function):
        return f"""|{func.name}|{', '.join(func.parameters)}|{func.description}|"""

    def varMD(self,var:Variable)->str:
        return f'''| {var.name} | {var.value}| {var.description}|\n'''

    def classMD(self,cls:Class) -> str:
        md =  f"""
## {cls.name}
### Attributes
"""
        if cls.attributes != []:
            md += """
| Name     | Value   | Description   |
| -------- | ------- |------- |
"""
            for i in cls.attributes:
                md += f"""|{i.name}|{i.value}| {i.description}|
"""
        else:
            md += f'''
This class does not have any attributes.
'''
        md += '''
### Methods
'''
        if cls.attributes != []:
            md += f'''
| Name     | Parameters   | Description   |
| -------- | ------- |------- |
'''
            for i in cls.methods:
                md += f"""|{i.name}|{', '.join(i.parameters)}| {i.description}|
"""
        else:
            md += f'''
This class does not have any methods.
'''
        return md
        

    def combineMD(self):
        

        md = f'''
# Documentation for {self.file_name}
# Classes
'''
        tree = self.makeTree()
        if tree['classes'] != []:
            for i in tree['classes']:
                md += self.classMD(i)
        else:
            md += f'''
This file does not contain any class definitions
'''
        md += '''
# Functions'''
        if tree['functions'] != []:
            md += f'''

| Name     | Parameters   | Description   |
| -------- | ------- |------- |
'''
            for i in tree['functions']:
                md+= self.funcMD(i)
        else:
            md += f'''
This file does not contain any function definitions
'''
        md += '''
# Variabless'''
        if tree['variables'] != []:
            md += f'''

| Name     | Value   | Description   |
| -------- | ------- |------- |
'''
            for i in tree['variables']:
                md+= self.varMD(i)
        else:
            md += f'''
This file does not contain any variable declarations
'''
        return md
    def makeMD(self):
        mdName = '.'.join(self.file_name.split('.')[:-1]) + '.md'
        f = open(mdName, "w")
        f.write(self.combineMD())
        f.close()
x = Parser('pydoc_parser.py') 
x.makeMD()

