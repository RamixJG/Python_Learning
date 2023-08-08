from pathlib import Path


paths = [
    Path.cwd() / f'reports/2020/{str(i).zfill(2)}_sales'
    for i in range(1, 13)
]

for path in paths:
    path.mkdir(parents=True)

 
for dir in sorted(Path.cwd().joinpath('reports/2020').iterdir()):
    print(dir)