def phone_formatter(number: int):
    """Phone formatter function.

    Format any 10 digit phone number to USA standard.
    """
    if type(number) != int:
        return None
    
    number = str(number)

    if len(number) != 10:
        print("Only 10 numbers, please.")
        return None
    
    return f'({number[0:3]}) {number[3:6]}-{number[6:]}'

if __name__ == "__main__":
    number = int(input("What's Your Number? "))
    print(phone_formatter(number))