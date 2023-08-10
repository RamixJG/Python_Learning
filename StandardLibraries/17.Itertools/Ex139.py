import itertools

iterator = itertools.repeat("#")

for item in range(10):
    print(next(iterator))