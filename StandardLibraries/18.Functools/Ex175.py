def fv(pv, r, n):

    fut_val = pv * (1+r)**n

    return round(fut_val,2)

print(fv(1000,0.04,1))
print(fv(1000,0.04,2))
print(fv(1000,0.03,5))
print(fv(10000,0.09,10))