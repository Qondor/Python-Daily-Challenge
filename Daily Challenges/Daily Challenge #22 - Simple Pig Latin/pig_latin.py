def pig_latin_converter(input_text):
    """Simple pig latin converter.

    Moves first letter of a word to the end of the word and adds "ay".
    """
    input_text = input_text.split()
    final_words = ""

    for words in input_text:
        words = list(words)
        words[-1] = words[0]
        words.remove(words[0])
        words.append("ay")
        final_words += "".join(words) + f' '
    return final_words

if __name__ == "__main__":
    print(pig_latin_converter("Hello there friends"))