import itertools

eurusd = [1.18425, 1.17928, 1.17211, 1.17505]
revenues = [20000, 21000, 20500, 18000, 22000, 25000]

for rate, revenue in itertools.zip_longest(eurusd, revenues):
    print(rate, revenue)