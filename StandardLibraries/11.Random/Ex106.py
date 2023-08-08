import random

random.seed(42)

numbers = [round(random.uniform(5,10), 4) for _ in range(10)]

print(numbers)