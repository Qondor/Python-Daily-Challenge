def century_calculator(century):
    """Century calculator.

    Takes any year as an input and returns century.
    """
    result = ""
    if century < 100:
        return "1st"
    else:
        result = str(int(century/100) + 1)
    if result[-1] == "1":
        return f'{result}st'
    elif result[-1] == "2":
        return f'{result}nd'
    elif result[-1] == "3":
        return f'{result}rd'
    else:
        return f'{result}th'
if __name__ == "__main__":
    print(century_calculator(100))


# 1st
# 2nd
# 3rd
# 4th
# 5th
# 6th
# 7th
# 8th
# 9th
# 10th
# 20th
# 30th