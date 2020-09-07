def pizza(min_orders, min_price):
    customers = {
    'John Doe' : [22, 30, 11, 17, 15, 52, 27, 12], 
    'Jane Doe' : [5, 17, 30, 33, 40, 22, 26, 10, 11, 45],
    'Joey Bonzo' : [22, 67, 53, 29],
    'Jennifer Bonzo' : [51, 19],
    'Natsumi Sakamoto' : [15, 15, 14],
    'Gorou Hironaka' : [15, 15, 15],
    'Shinju Tanabe' : [120, 240]
    }
    x = 0
    result = []
    for customer, orders in customers.items():
        for order in orders:
            if order >= min_price:
                x += 1
        if x >= min_orders:
            result.append(customer)
        x = 0
    return result

if __name__ == "__main__":
    print(pizza(5, 20))