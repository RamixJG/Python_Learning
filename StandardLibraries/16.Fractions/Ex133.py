from fractions import Fraction
import math

f1 = Fraction(1,4)

print(f"{f1} ** 2 = {f1**2}")
print(f"{f1} ** 3 = {f1**3}")
print(f"math.sqrt({f1}) = {math.sqrt(f1)}")
print(f"math.sqrt(Fraction({f1})) = {Fraction(math.sqrt(f1))}")