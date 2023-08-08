from pathlib import Path
from pprint import pprint
import random


random.seed(42)
paths_dict = {}

paths = [
    Path.cwd() / f'media/music/playlist_{str(i).zfill(2)}'
    for i in range(1, 6)
]

for path in paths:
    path.mkdir(parents=True)

ext = [".mp3", ".wav"]

for path in paths:
    files = [f"0{str(i)}_music.{random.choice(ext)}"
             for i in range(1,6)]
    paths_dict[path] = files

pprint(paths_dict)