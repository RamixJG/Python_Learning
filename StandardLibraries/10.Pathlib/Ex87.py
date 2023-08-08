from pathlib import Path

work_dir = Path.cwd()
path = Path.cwd() / "reports"

if not path.is_dir():
    path.mkdir()

items = work_dir.iterdir()

for item in sorted(items):
    print(item)