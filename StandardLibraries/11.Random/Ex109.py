import random


techs = ['python', 'java', 'php', 'c++', 'c#', 'javascript']

random.seed(32)

print(random.choices(techs,k=3))