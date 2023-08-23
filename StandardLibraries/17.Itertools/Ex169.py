import itertools


data = [
    {"user": "0032", "level": 70},
    {"user": "0034", "level": 74},
    {"user": "0233", "level": 71},
    {"user": "0532", "level": 70},
    {"user": "0634", "level": 74},
    {"user": "0245", "level": 70},
    {"user": "0235", "level": 70},
    {"user": "0255", "level": 71},
]

sordata = sorted(data, key=lambda x: x["level"])
grouped_data = itertools.groupby(sordata, key=lambda x: x["level"])

for key, group in grouped_data:
    user_list = [entry["user"] for entry in group]  # Extract user values from each entry
    print(f"{key} -> {user_list}")