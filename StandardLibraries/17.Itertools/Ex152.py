import itertools


stocks = ['Apple', 'Microsoft', 'Amazon', 'Google', 'Adidas', 'Audi', 'Siemens']

stocks_flag = [item.startswith("A") for item in stocks]

for item in list(itertools.compress(stocks,stocks_flag)):
    print(item)