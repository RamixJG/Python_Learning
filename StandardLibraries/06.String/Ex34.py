import string

docs = 'programming in python'
# Generating lowercase ascii characters
values = string.ascii_lowercase

# Creating dictionary and its inverse
code_map = {}

for index, letter in enumerate(values):
    code_map[index] = letter

# Handier way to create the dictionary
# code_map = dict((enumerate(string.ascii_lowercase)))

code_map_inv = {value: key for key, value in code_map.items()}

mapped_chars = []
result = ''
# Map each character in the input string using the replacement dictionary
for char in docs:
    if char == ' ':
        result += ' '
        continue
    idx = (code_map_inv[char] + 3) % 26
    result += code_map[idx]

print(result)