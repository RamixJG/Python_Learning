from pathlib import Path

path = Path.cwd() / "reports/ecommerce/2020/01"

path.mkdir(parents=True)

print(path.is_dir())