from collections import Counter


poll_1 = {'yes': 140, 'no': 120, None: 12}
poll_2 = {'yes': 113, 'no': 132, None: 9}
poll_3 = {'yes': 16, 'no': 14}

poll1 = Counter(poll_1)
poll2 = Counter(poll_2)
poll3 = Counter(poll_3)

pollsum = poll1 + poll2 + poll3

# print(pollsum.get('yes'))
print(pollsum['yes'])