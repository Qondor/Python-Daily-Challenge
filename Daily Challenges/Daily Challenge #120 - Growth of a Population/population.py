def nb_year(p0, percent, aug, p):
    """In a small town, the population is p0 at the beginning of a year. The population regularly increases by X percent per year and moreover Z new inhabitants per year come to live in the town.

    How many years does the town need to see its population greater or equal to p inhabitants?
    """
    years = 0
    percent /= 100
    while p0 < p:
        p0 = p0 + (p0 * percent) + aug
        years += 1
    return years


if __name__ == "__main__":
    print(nb_year(1500, 5, 100, 5000))