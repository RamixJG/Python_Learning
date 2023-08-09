import numbers


class Phone:
    
    def __init__(self, price):
        if isinstance(price, numbers.Number) and price >= 0:
            self.price = price
        else:
            raise TypeError("'value' must be a positive number.")

