import itertools


fnames = [
    "01_image.jpg",
    "02_image.png",
    "03_image.jpg",
    "04_image.jpg",
    "05_image.jpg",
    "06_image.png",
    "07_image.jpg",
    "08_image.png",
    "09_image.svg",
    "10_image.svg",
    "11_image.jpeg",
    "12_image.jpeg",
]

func = lambda fname: fname.split(".")[-1]

sordata = sorted(fnames, key=func)

grouped_data = itertools.groupby(sordata, key=func)

for key, group in grouped_data:
    print(f"{key} -> {len(list(group))}")