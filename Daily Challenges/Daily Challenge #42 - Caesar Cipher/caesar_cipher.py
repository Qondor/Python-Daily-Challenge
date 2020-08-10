def caesar_cipher_decrypter(input_text):
    """Caesar Cipher decrypter.

    Takes any string and moves any letter by 1 in the alphabet - letter "z" turns into "a" to wrap things up.
    """
    letter = 0
    result = ""
    input_text = list(input_text)
    while letter < len(input_text):
        if input_text[letter].isalpha() == True:
            temp = ord(input_text[letter])
            # Checking if character is letter "z" - if so, it is changed into "a" like true Caesar Cipher would do
            temp += 1
            if temp == 123:
                temp = 97
            input_text[letter] = chr(temp)
        letter += 1
    return result.join(input_text)

if __name__ == "__main__":
    print(caesar_cipher_decrypter("I like sword - that's a personal weapon."))