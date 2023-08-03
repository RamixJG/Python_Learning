from collections import Counter


text = 'python programming - introduction'

cnt = Counter(text)


print(cnt.most_common(3))