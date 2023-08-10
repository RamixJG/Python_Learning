import decimal
 
 
print(round(19.345, 2))
 
number = decimal.Decimal(19.345)
result = round(number, 2)
print(result)
 
result = decimal.Decimal(number).quantize(
    decimal.Decimal('0.00'), 
    rounding=decimal.ROUND_UP
)
print(result)