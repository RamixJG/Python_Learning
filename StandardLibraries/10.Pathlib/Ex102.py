from pathlib import Path
 
 
path = Path.cwd() / 'README.md'
 
with path.open('r') as file:
    headers = [line.strip() for line in file if line.startswith('#')]
print('\n'.join(headers))