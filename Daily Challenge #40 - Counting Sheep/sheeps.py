import inflect
p = inflect.engine()

def sheep_counter(number_of_sheeps):
    """Sheeps counter.

    Counts sheeps until user falls asleep. 🐑 Baaah!
    """
    counter = 2
    result = "one sheep... \n"
    while counter <= number_of_sheeps:
        result += f'{p.number_to_words(counter)} sheeps... \n'
        counter += 1
    result += "Zzz..."
    return result

if __name__ == "__main__":
    print(sheep_counter(6))