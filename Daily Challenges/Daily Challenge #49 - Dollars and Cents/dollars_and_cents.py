def dollars(input_float):
    input_float = str(input_float)
    if input_float[-2] == ".":
        return f'${input_float}0'
    return f'${input_float}'

if __name__ == "__main__":
    print(dollars(6.2))