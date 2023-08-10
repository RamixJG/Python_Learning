import itertools

iterator = itertools.count(start=0)

for item in range(10):
    print(next(iterator))