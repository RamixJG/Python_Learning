import itertools

values = [(44, 7), (57, 6), (10, 3)]

for value in itertools.starmap(lambda x,y: x%y, values):
    print(value)