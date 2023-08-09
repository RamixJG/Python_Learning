import decimal

m = decimal.Decimal(0.1)
n = decimal.Decimal(0.2)

with decimal.localcontext() as ctx:
    ctx.prec = 40
    print(n+m)

print(n+m)