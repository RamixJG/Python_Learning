from functools import reduce


numbers_1 = [5, 2, 3, 4, 0, 6]
numbers_2 = [5, 2, 3, 4, 1, 6]

print(reduce(lambda x,y: bool(x and y), numbers_1))
print(reduce(lambda x,y: bool(x and y), numbers_2))