import numbers

values = [2.0, 2, '2.0', '2', None, False, True]

for value in values:
    print(f"{str(value):<5}: {str(type(value)):<20}: {isinstance(value,numbers.Number)}")