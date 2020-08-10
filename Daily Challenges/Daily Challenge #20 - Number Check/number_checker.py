def num_check(input_number):
    """Number checker.

    Checks if number is prime, even and a multiple of 10, and returns True/False for each in list.
    """
    return [
        is_prime(input_number),
        is_divisible_by(input_number, 2),
        is_divisible_by(input_number, 10)
    ]

    prime = 0
    result = []
    if input_number > 1:
        for i in range(2, input_number):
            if (input_number % i) == 0: 
                prime += 1
        if prime >= 1:
            result.append(False)
        else:
            result.append(True)

    if (input_number % 2) == 0:
        result.append(True)
    else:
        result.append(False)

    if (input_number % 10) == 0:
        result.append(True)
    else:
        result.append(False)

    return result

if __name__ == "__main__":
    print(num_check(10))