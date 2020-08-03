import inflect
p = inflect.engine()

def wordify(number):
    """Converter of numbers to words.

    Converts numbers to words.
    """
    return p.number_to_words(number)

if __name__ == "__main__":
    print(wordify(56))