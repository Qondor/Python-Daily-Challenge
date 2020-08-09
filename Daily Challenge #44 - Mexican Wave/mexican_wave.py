def wave(input_text):
    """Mexican Wave generator.

    Takes a string and returns it changed into Mexican Wave - every letter in sequence gets upppercased.
    """
    x = 0
    temp = []
    result = []
    input_text = list(input_text)
    while x < len(input_text):
        temp = input_text[:]
        temp[x] = temp[x].upper()
        temp = "".join(temp)
        result.append(temp)
        x += 1
    return result

if __name__ == "__main__":
    print(wave("bucciarati"))