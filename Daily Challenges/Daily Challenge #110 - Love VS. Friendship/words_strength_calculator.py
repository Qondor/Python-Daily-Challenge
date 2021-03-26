def wordsToMarks(word):
    """If　a = 1, b = 2, c = 3 ... z = 26, then l + o + v + e = 54

    Function to find the "strength" of each of these values.
    """

    value = []
    value.extend((ord(letter) - 96) for letter in word)
    return sum(value)



if __name__ == "__main__":
    print(wordsToMarks("attitude"))