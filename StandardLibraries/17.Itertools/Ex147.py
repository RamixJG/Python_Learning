import itertools


stocks_us = ['Apple', 'Microsoft', 'Amazon', 'Google']
stocks_de = ['Adidas', 'Audi', 'Siemens']

results = itertools.chain(stocks_us,stocks_de)

for result in results:
    print(result)