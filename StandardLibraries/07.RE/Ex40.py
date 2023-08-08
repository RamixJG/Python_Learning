import re

code = 'PL code: XG-GH-110'

pattern = r"\w+$|^\w+"

print(re.findall(pattern, code))