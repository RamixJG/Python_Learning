import itertools

lett = ['a', 'b', 'c']
num = [1,2,3]

iterator = itertools.product(lett,num)

iter1, iter2 = itertools.tee(iterator, 2)

print(list(iter1))
print(list(iter2))