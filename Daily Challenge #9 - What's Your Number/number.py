def phone_formatter():
    number = int(input("What's Your Number? "))
    if len(str(number)) != 10:
        print("Only 10 numbers, please.")
    print(number)

phone_formatter()