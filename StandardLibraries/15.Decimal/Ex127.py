import decimal

decimal.getcontext().prec = 40

print(decimal.Decimal(0.1)+decimal.Decimal(0.2))