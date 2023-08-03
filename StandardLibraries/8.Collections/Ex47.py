from collections import Counter


poll_1 = {'yes': 140, 'no': 120, None: 12}
poll_2 = {'yes': 113, 'no': 132, None: 9}

poll1 = Counter(poll_1)
poll2 = Counter(poll_2)

pollsum = poll1 + poll2

print(pollsum)