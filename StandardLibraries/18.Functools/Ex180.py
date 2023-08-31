from functools import reduce


numbers = [5, 2, 3, 4, 1, 6]

print(reduce(lambda x,y: x+y,numbers,10))