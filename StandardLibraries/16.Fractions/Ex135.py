from fractions import Fraction
import math

print(f"""limit: 10
\tpi = {Fraction(math.pi).limit_denominator(10)}
\te = {Fraction(math.e).limit_denominator(10)}
limit: 100
\tpi = {Fraction(math.pi).limit_denominator(100)}
\te = {Fraction(math.e).limit_denominator(100)}
limit: 1000
\tpi = {Fraction(math.pi).limit_denominator(1000)}
\te = {Fraction(math.e).limit_denominator(1000)}
""")