import itertools


stream1 = [0.5, 9.9, 8.53, 4.6, 5.58, 7.07, None, 4.5, 3.61, 9.31]
stream2 = [3.75, 9.51, 7.32, None, 1.56, 1.56, 0.58, 8.66, 6.01, 7.08]

results = itertools.chain(itertools.takewhile(lambda value: value != None, stream1), itertools.takewhile(lambda value: value != None, stream2))

for element in results:
    print(element)