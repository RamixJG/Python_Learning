import random

random.seed(42)

numbers =[]
for i in range(0,10):
    numbers.append(round(random.random(),4))

# numbers = [round(random.random(), 4) for _ in range(10)]

print(numbers)