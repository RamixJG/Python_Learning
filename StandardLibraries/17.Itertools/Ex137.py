import itertools

iterator = itertools.count(start=1,step=2)

for item in range(5):
    print(next(iterator))