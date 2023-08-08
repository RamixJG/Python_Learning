from pathlib import Path

paths = [
    Path.cwd() / f'media/music/playlist_{str(i).zfill(2)}'
    for i in range(1, 11)
]

for path in paths:
    path.mkdir(parents=True)

for dir in sorted(Path.cwd().joinpath('media/music/').iterdir()):
    print(dir)