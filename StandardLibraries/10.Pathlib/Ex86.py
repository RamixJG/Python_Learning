from pathlib import Path


path = Path.home() / 'reports/2020/01/sales.csv'

for parent in path.parents:
    print(parent)