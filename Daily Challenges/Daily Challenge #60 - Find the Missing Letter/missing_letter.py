def letter(letter_list):
    x = 0
    result = ""
    while x < len(letter_list) - 1:
        if ord(letter_list[x]) - ord(letter_list[x+1]) != -1:
            result = chr(ord(letter_list[x+1]) - 1)
        x += 1
        
    return result

if __name__ == "__main__":
    print(letter(['a', 'b', 'c', 'd', 'f']))