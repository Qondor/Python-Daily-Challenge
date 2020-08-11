def alphabet_to_position(input_string):
    """Letter to position-in-alphabet converter.

    Takes any given string and gives back position of every letter in alphabet (a = 1).
    """
    input_string = list(input_string.lower())
    letter = 0
    result = []
    while letter < len(input_string):
        if input_string[letter].isalpha():
            input_string[letter] = ord(input_string[letter])
            input_string[letter] -= 96
            result.append(input_string[letter])
        letter += 1
    return result


if __name__ == "__main__":
    print(alphabet_to_position("The sunset sets at twelve o' clock."))