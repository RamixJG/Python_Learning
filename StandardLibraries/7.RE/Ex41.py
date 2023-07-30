import re


text = "Please send an email to info@template.com or sales-info@template.it"


pattern = r'[^@\s]+@[^@\s]+'

print(re.findall(pattern, text))