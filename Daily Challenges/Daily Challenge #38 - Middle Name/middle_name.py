def middle_name_shorter(name):
    """Middle name shorter.

    Takes any name and shortens middle name/names. If name contains only one or two words it is just returned.
    """
    if len(name.split()) <= 2:
        return name
    else:
        name = name.split()
        for x in range(1, len(name) - 1):
            name[x] = f'{name[x][0]}.'
    return " ".join(name)

if __name__ == "__main__":
    print(middle_name_shorter('Esteban Julio Ricardo Montoya de la Rosa Ramirez'))