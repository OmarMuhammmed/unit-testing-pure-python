def calculate_tax(price, tax_rate):
   
    if price < 0 or tax_rate < 0:
        raise ValueError("Invalid input. Price and tax rate must be non-negative.")
    return price + (price * tax_rate)
