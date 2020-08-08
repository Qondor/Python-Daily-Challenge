def word_spinner(input_words):
    """Word spinner.

    Takes a string and reverses words that are 5 characters long or longer.
    """
    input_words = input_words.split()
    reversed_list = []
    for word in input_words:
        if len(word) >= 5:
            reversed_list.append(f"{word[::-1]:}")
        else:
            reversed_list.append(f"{word}")
    reversed_string = " ".join(reversed_list)
    return reversed_string

print(word_spinner("Python XKCD AAADCKX One Two Fourteen"))