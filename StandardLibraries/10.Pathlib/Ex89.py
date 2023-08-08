from pathlib import Path
 
 
paths = [
    Path.cwd() / f'reports/2020/{str(i).zfill(2)}' 
    for i in range(1, 13)
]
 
for path in paths:
    path.mkdir(parents=True)
 
for dir in sorted(path.parent.iterdir()):
    print(dir)    