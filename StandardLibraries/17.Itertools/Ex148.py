import itertools


stocks_us = ['Apple', 'Microsoft', 'Amazon', 'Google']
stocks_de = ['Adidas', 'Audi', 'Siemens']
stocks = [stocks_us, stocks_de]

results = itertools.chain.from_iterable(stocks)

for result in results:
    print(result)