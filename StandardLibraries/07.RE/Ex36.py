import re


text = 'Python 3.8'

pattern = r"\d"

print(re.findall(pattern, text))
