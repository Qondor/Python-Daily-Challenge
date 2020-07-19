def cubic_checker(check_num):
    """Cubic number checker.

    Check if digits of your number raised to the power of three are equal to that number.
    """
    check_num = str(check_num)
    sum_of_cubs = 0
    for x in check_num:
        x = int(x)
        sum_of_cubs += x**3
    if sum_of_cubs == int(check_num):
        return f'Yes, {check_num} is a cubic number.'

if __name__ == "__main__":
    print(cubic_checker(153))