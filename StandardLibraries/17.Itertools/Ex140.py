import itertools


stocks = [
    "Apple",
    "Microsoft",
    "Amazon",
    "Google",
    "Adidas",
    "Audi",
    "Siemens",
]

comb = itertools.combinations(stocks,2)

for _ in comb:
    print(_)