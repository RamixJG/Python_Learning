from pathlib import Path
import re
 
 
pattern = r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+"
 
path = Path.cwd() / 'README.md'
content = path.read_text()
https = re.findall(pattern, content)
print('\n'.join(sorted((set(https)))))