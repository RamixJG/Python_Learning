eurusd = [1.18425, 1.17928, 1.17211, 1.17505, 1.16421, 1.15958]
revenues = [20000, 21000, 20500, 18000, 22000, 25000]

for item in list(zip(eurusd,revenues)):
    print(f"{item[0]} {item[1]}")

# for rate, revenue in zip(eurusd, revenues):
#     print(rate, revenue)