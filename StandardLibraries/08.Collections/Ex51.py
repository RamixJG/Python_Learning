from collections import Counter
import re


text = """"Python is fast enough for our site and allows us to produce maintainable features in record times,
with a minimum of developers," said Cuong Do, Software Architect, YouTube.com.

"Python plays a key role in our production pipeline. Without it a project the size of Star Wars:
Episode II would have been very difficult to pull off. From crowd rendering to batch processing to compositing,
Python binds all things together," said Tommy Burnette, Senior Technical Director, Industrial Light & Magic."""


# Create pattern for re and split the text
pattern = r"\b\w+\b"

text_split = re.findall(pattern, text)

# Make lowercase
for idx, word in enumerate(text_split): text_split[idx] = word.lower() 

cnt = Counter(text_split)

print(cnt.most_common(3))