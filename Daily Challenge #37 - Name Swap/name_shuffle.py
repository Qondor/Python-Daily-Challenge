def name_shuffler(name):
    """Name shuffler.

    Changes place of first and last name.
    """
    name = name.split()
    return f'{name[-1]} {name[0]}'

if __name__ == "__main__":
    print(name_shuffler('Emma McClane'))