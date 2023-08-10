import itertools

iterator = itertools.cycle([-1,0,1])

for item in range(15):
    print(next(iterator))