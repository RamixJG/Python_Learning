import itertools

data = [1, 5, 3, 4, 6, 9, 3]

grouped_data = itertools.groupby(data, key=lambda x: 'even' if x % 2 == 0 else 'odd')

for key, group in grouped_data:
    print(f"{key} -> {list(group)}")