def even(numbers):
    """Even and odd number total value calculator.
    
    Given a string of numbers confirm whether the total of all the individual even numbers are greater than the total of all the individual odd numbers.
    """
    numbers = list(numbers)
    total_even = 0
    total_odd = 0
    for number in numbers:
        if int(number) % 2 == 0:
            total_even += int(number)
        else:
            total_odd += int(number)
    
    if total_even > total_odd:
        return "Even is greater than Odd"
    elif total_odd > total_even:
        return 'Odd is greater than Even'
    else:
        return 'Even and Odd are the same'

if __name__ == "__main__":
    print(even("11114"))