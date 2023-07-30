import re


text = 'Python 3.8'

pattern = r"\D"

print(re.findall(pattern, text))