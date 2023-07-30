import re

code = '0010-000-423'

pattern = r"[1-9]"

print(re.findall(pattern, code))