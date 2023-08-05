from pathlib import Path

home = Path.home()
cwd = Path.cwd()

# path1 = Path.joinpath(home, "reports/2020/01/sales.csv")
path1 = Path.home() / 'reports/2020/01/sales.csv'
path2 = Path.joinpath(cwd, "reports/2020/01/sales.csv")

print(path1)
print(path2)