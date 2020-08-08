def iteration_calculator(drinker, iteration):
    """Assistant function to main Cola Drinker Calculator.

    Calculates iteration of drinker.
    """
    iteration = 0
    previous_iterations = 0
    while iteration <= drinker:
        if (5 * 2**iteration) + previous_iterations >= drinker:
            drinker -= previous_iterations
            return drinker, iteration
        else:
            previous_iterations += 5 * 2**iteration
            iteration += 1

def cola_drinker_calculator(drinker):
    """Cola drinker calculator.

    Calculates the n-th cola drinker - Sheldon, Leonard, Penny, Rajesh or Howard.
    """
    cola_drinkers = {0: "Sheldon", 1: "Leonard", 2: "Penny", 3: "Rajesh", 4: "Howard"}
    name_number = 0
    nth_drinker = []
    drinker, iteration = iteration_calculator(drinker, 0)
    for current_name in ("0","1","2","3","4"):
        while name_number < 2**iteration:
            nth_drinker.append(current_name)
            name_number += 1
        name_number = 0
    drinker -= 1
    return cola_drinkers[int(nth_drinker[drinker])]

if __name__ == "__main__":
    print(cola_drinker_calculator(6))