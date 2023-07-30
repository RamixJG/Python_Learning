import re


text = (
    "Please send an email to info@template.com or "
    "call to: 123-456-789."
)

pattern = r'\d+[-]\d+[-]\d+'
rep = "***-***-***"

print(re.sub(pattern, rep , text))