# Documentation for pydoc_parser.py
# Classes

## Parser
### Attributes
| Name     | Value   |
| -------- | ------- |
|file_name|file_name|
|file|open(file_name,"r")|
|trial|'x'|

### Methods
| Name     | Parameters   |
| -------- | ------- |
|__init__|self, file_name|
|find_level|self, line|
|parse|self, line|
|makeTree|self|
|show|self|
|funcMD|self, func|
|combineMD|self|

# Functions
| Name     | Parameters   |
| -------- | ------- |
|trial|x, y|
# Variables
| Name     | Value   |
| -------- | ------- |
| x | Parser('pydoc_parser.py')|