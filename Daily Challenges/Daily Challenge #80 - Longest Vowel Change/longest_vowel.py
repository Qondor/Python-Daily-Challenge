def vowel(word):
    """Longest vowel substring in given string calculator.
    
    Given a lowercase string that has alphabetic characters only and no spaces, returns the length of the longest vowel substring.
    """
    word = list(word)
    vowels = {"a", "e", "i", "o", "u"}
    x = 0
    while x < len(word):
        if set(word[x]).issubset(vowels) == False:
            word[x] = " "
        x += 1
    result = "".join(word)
    result = result.split(" ")
    return len(max(result, key=len))


if __name__ == "__main__":
    print(vowel("codewarriors"))