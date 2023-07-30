import re


message = 'For more information, please call: 123-456-789'

pattern = r'\d+[-]\d+[-]\d+'

print(re.findall(pattern, message)[0])