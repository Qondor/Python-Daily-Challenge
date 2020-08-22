def change(order, money):
    """Bob's Coffee Shop order and change automat.

    Returns client ordered coffee when given exact amount of money, if not, asks to return the next day.
    """
    menu = {
        "Americano" : 2.20,
        "Latte" : 2.30,
        "Flat white" : 2.40,
        "Filter" : 3.50
    }
    if menu[order] == money:
        return f'Here is your {order}, have a nice day!'
    else:
        return "Sorry, exact change only, try again tomorrow!"

if __name__ == "__main__":
    print(change("Americano", 2.20))