import re
def vowel_counter():
    """Vowel counter.

    Counts vowels in any given text.
    """
    input_text = input("Write text to count vowels: ")
    vowel_list = re.findall("[aeiou]", input_text, flags = re.I)
    countered_vowels = len(vowel_list)
    return countered_vowels

if __name__ == "__main__":
    print(vowel_counter())