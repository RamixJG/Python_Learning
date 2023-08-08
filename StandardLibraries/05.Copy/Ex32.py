import copy

# Define a list and copy it
stocks = [['CDR', '11B'], ['PLW'], ['TEN']]
stocks_copied = copy.copy(stocks)

# Modify list
stocks[0][1] = 'CRJ'

# Print lists
print(f'stocks: {stocks}')

print(f'stocks_copied: {stocks_copied}')