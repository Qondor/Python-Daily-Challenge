def word_spinner(input_words):
    """Word spinner function.

    """
    input_words = input_words.split()
    reversed_words = []
    print(input_words)
    for word in input_words:
        if len(word) >= 5 and word != input_words[-1]:
            reversed_words.append(word[::-1])
        elif len(word) > 5 and word == input_words[-1]:
            word.split()
            
            reversed_words.append(word[::-1])
        elif len(word) <= 5 and word == input_words[-1]:
            reversed_words.append(word)
        else:
            reversed_words.append(word)
    return reversed_words

print(word_spinner("Testable stingerino alb 2123."))