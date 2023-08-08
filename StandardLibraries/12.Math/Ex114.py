import math

def calculate_seq(n):
    a_n = math.pow( 1+1/n, n)
    return a_n

check = True
n = 1

while check:
    
    if math.isclose(math.e, calculate_seq(n), rel_tol=1e-06):
        print(n)
        check = False
    else:
        n +=1