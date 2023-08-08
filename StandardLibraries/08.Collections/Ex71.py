from collections import defaultdict


transactions = [
    ('001', 100),
    ('003', 10),
    ('002', 80),
    ('001', 90),
    ('002', 46),
    ('001', 43),
    ('003', 23),
]


def_dict = defaultdict(int)

for customer, value in transactions:
    def_dict[customer] += value

print(def_dict)