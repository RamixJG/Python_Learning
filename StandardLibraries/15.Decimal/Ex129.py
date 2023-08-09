import decimal

print(round(19.345,2))

num = decimal.Decimal(19.345)
print(round(num,2))

print(num.quantize(decimal.Decimal('0.00'),rounding=decimal.ROUND_UP))

