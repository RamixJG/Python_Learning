import math
 
def prob(k):
    hits = math.comb(6, k) * math.comb(49 - 6, 6 - k)
    result = hits / math.comb(49, 6)
    return result

for i in range(6, -1, -1):
    print(f'hit: {i} prob: {100 * prob(i):.10f}%')
