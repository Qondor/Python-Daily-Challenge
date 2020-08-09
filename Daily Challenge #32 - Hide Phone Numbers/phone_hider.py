def phone_number_hider(number):
    number = list(number)
    for x in range(5, 12):
        if number[x].isnumeric():
            number[x] = "X"
    number = "".join(number)
    return number

if __name__ == "__main__":
    print(phone_number_hider("201-680-0202"))