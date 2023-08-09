from statistics import NormalDist

normal = NormalDist(170,15)

print(f"Probability: {(normal.cdf(180)- normal.cdf(170))*100:.2f}%")