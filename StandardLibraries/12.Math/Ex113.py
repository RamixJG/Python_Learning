import math

def calculate_seq(n):
    a_n = math.pow( 1+1/n, n)
    print(a_n)

for i in range(1,21):
    calculate_seq(i)