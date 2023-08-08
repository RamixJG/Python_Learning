from pathlib import Path
 
 
paths = [
    Path.cwd() / f'reports/2020/{str(i).zfill(2)}_sales'
    for i in range(1, 13)
]
 
t = 3
targets = [
    Path.cwd()
    / f'reports/2020/Q{i // t}/{str(i - t + 1).zfill(2)}_sales'
    for i in range(t, t + 12)
]
for target in targets:
    print(target)