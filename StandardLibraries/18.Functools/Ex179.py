from functools import reduce
 
 
numbers = [5, 2, 3, 4, 1, 6]
letters = ['P', 'y', 't', 'h', 'o', 'n']
 
print(reduce(lambda x, y: x + y, numbers))
print(reduce(lambda x, y: x + y, letters))