import inflect
p = inflect.engine()

def wordify(number):
    return p.number_to_words(number)

if __name__ == "__main__":
    print(wordify(56))