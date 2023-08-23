import itertools


fnames = [
    "01_image.jpg",
    "02_image.png",
    "03_image.jpg",
    "04_image.jpg",
    "05_image.jpg",
    "06_image.png",
    "07_image.jpg",
    "08_image.jpg",
]

sordata = sorted(fnames, key=lambda x: str(x).endswith(".png"))

grouped_data = itertools.groupby(sordata, key=lambda x: '.jpg' if str(x).endswith(".jpg") else '.png')

for key, group in grouped_data:
    print(f"{key} -> {list(group)}")