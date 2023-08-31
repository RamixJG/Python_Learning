def fv(pv, r, n, m =1):

    fut_val = pv * (1+r/m)**(n*m)

    return round(fut_val,2)

print(fv(1000,0.04,1))
print(fv(1000,0.04,1,2))
print(fv(1000,0.04,1,4))
print(fv(1000,0.04,1,12))