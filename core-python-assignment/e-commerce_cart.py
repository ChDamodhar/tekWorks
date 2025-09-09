def total_price(items):
    if not items:
        return 0 
    total = sum(items.values())
    if len(items) > 5:
        total *= 0.9  
    return int(total)
items = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}
total_price = total_price(items)
print("Total Price:", total_price)
