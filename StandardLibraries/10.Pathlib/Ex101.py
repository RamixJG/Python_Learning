from pathlib import Path
from pprint import pprint
import random
 
 
random.seed(42)
paths = [
    Path.cwd() / f'media/music/playlist_{str(i).zfill(2)}' 
    for i in range(1, 7)
]
 
for path in paths:
    path.mkdir(parents=True)
 
paths_dict = {
    path: [f"{str(i).zfill(2)}_music.{random.choice(['mp3', 'wav'])}" 
    for i in range(1, 6)] for path in paths
}
 
fname_paths = []
for path, fnames in paths_dict.items():
    for fname in fnames:
        fname_paths.append(path.joinpath(fname))
 
for fname_path in fname_paths:
    fname_path.touch()
 
path = Path.cwd() / 'media/music/playlist_05'
fnames_mp3 = list(path.glob('*.mp3'))
fnames_wav = list(path.glob('*.wav'))
 
print(f'fnames_mp3: {len(fnames_mp3)}')
print(f'fnames_wav: {len(fnames_wav)}')