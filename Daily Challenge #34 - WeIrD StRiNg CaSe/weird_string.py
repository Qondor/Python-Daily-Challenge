def weird_string_converter(input_text):
    x = 0
    result = ""
    while x < len(input_text):
        if x % 2 == 0:
            result += input_text[x].upper()
        else:
            result += input_text[x].lower()
        x += 1
    return result

if __name__ == "__main__":
    print(weird_string_converter("Moim zdaniem to nie ma tak, że dobrze albo że nie dobrze."))