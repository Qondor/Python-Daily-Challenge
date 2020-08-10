def virus_remover(input_text):
    """

    """
    x = 0
    result = ""
    changed_word = ""
    if input_text[-1] == ".":
        input_text = input_text[0] + input_text[1:-1].lower() + "."
    else:
        input_text = input_text[0] + input_text[1:-1].lower()
    input_text = input_text.split()
    for word in input_text:
        while x < (len(word) - 1):
            if word[x] == "i" and word[x+1] == "e":
                word = list(word)
                temp = word[x]
                word[x] = word[x+1]
                word[x+1] = temp
                word = changed_word.join(word)
                
            x += 1
        x = 0
        result += f'{word} '
    
    
    
    return result


if __name__ == "__main__":
    print(virus_remover("Ie haD iEght ShOTs of CAffIEne."))