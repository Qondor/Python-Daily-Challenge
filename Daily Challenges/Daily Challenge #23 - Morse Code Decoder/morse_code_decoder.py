def MORSE_CODE(input_text, direction):
    """Morse code converter.

    Can translate from Morse code to letters.
    """
    letters_to_morse = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'}

    morse_to_letters = { value:key for key, value in letters_to_morse.items()}

    input_text = input_text.split()

    result = ""
    for letter in input_text:
        if direction == "m_t_l":
            result += morse_to_letters[letter]
        else:
            result += letters_to_morse[letter]
    return result

if __name__ == "__main__":
    print(MORSE_CODE(".... . -.-- .--- ..- -.. .", "m_t_l"))