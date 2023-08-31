from functools import reduce


numbers_1 = [0, 0, '', None, []]
numbers_2 = [5, 2, 3, 4, 1, 6]

print(reduce(lambda x,y: bool(x or y), numbers_1))
print(reduce(lambda x,y: bool(x or y), numbers_2))