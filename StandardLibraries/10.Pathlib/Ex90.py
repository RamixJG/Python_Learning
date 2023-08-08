from pathlib import Path


path = Path.cwd() / 'hello.txt'

if not path.exists():
    with open(path,"w") as file:
        file.write("Open,High,Low,Close")


with open(path,"r") as file:
        content = file.read()

print(content)