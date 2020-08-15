def num_neighbours(phone_number):
    """Phone number neighbours calculator.

    Show your previous and next phone number neighbour.
    """

    prev_neighbour = phone_number - 1
    prev_neighbour = str(prev_neighbour)
    next_neighbour = phone_number + 1
    next_neighbour = str(next_neighbour)
    phone_number = str(phone_number)
    if len(prev_neighbour) < 10:
        prev_neighbour = "0" + prev_neighbou
    your_number = f'{phone_number[0:3]}-{phone_number[3:6]}-{phone_number[6:10]}'
    prev_neighbour = f'{prev_neighbour[0:3]}-{prev_neighbour[3:6]}-{prev_neighbour[6:10]}'
    next_neighbour = f'{next_neighbour[0:3]}-{next_neighbour[3:6]}-{next_neighbour[6:10]}'
    return f'Your number: {your_number}\nFirst neighbour: {prev_neighbour}\nSecond neighbour: {next_neighbour}'

if __name__ == "__main__":
    print(num_neighbours(6659203410))