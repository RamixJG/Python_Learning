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

comb = itertools.combinations_with_replacement(stocks,2)

for _ in comb:
    print(_)