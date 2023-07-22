import datetime as dt

# Financial parameter
rate = 0.04     # yearly rate
pv = 1000       # present value of the investment

# Beginning and ending date of investment
dtb = dt.datetime(2021,7,1)
dte = dt.datetime(2021,12,31)

# Dates difference
diff = (dte-dtb).days

# Future value formula
fv = pv*(1 + rate/365)**diff

print(f"Future value: $ {round(fv,2)}")