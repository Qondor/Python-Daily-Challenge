def question_remover(input_text):
    """Question mark remover.

    Removes question marks from any given string, even if there are few question marks next to each other.
    """
    input_text = list(input_text)
    x = 0
    while x < len(input_text):
        if input_text[x] == "?":
            input_text.remove(input_text[x])
            x -= 1
        x += 1
    return "".join(input_text)

if __name__ == "__main__":
    print(question_remover("Are you there? Hello??? That's weird."))