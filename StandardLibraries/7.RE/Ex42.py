import re


text = """Python plays a key role in our production pipeline.
Without it a project the size of Star Wars: Episode II would have been very difficult to pull off."""

pattern = r'\w+'

print(re.findall(pattern, text))