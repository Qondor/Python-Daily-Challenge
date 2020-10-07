def camelcase(input_text):
    """Camel Case text generator.

    All words must have their first letter capitalized without spaces.
    """
    words = input_text.split()
    result = ""
    for word in words:
        result += f'{word[0].upper()}{word[1:]}'
    return result


if __name__ == "__main__":
    print(camelcase("oh camel camel texterino"))