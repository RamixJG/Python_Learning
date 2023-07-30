import re

code = '0010-000-423-22'

pattern = r"\d+"

print(re.findall(pattern, code))