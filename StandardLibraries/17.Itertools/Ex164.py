import itertools

data = [1, 5, 3, 4, 6, 9, 3]

sordata = sorted(data, key=lambda x: x%2)

grouped_data = itertools.groupby(sordata, key=lambda x: 'even' if x % 2 == 0 else 'odd')

for key, group in grouped_data:
    print(f"{key} -> {list(group)}")