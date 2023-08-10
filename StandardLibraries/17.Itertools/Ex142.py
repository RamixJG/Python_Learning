import itertools

names = ['Bob', 'Mark', 'Guido']

perm = itertools.permutations(names)

for _ in perm:
    print(_)