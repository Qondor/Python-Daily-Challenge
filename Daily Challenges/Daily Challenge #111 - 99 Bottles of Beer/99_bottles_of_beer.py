def beer(initial_bottles):
    """Y'all know the lyrics to the song "99 Bottles of Beer on the Wall", right? Instead of removing just one bottle in each iteration, we want to remove one more bottle than in the previous iteration (i.e. start with 99, then 98, then 96, 93, 89, etc.).

    A function that takes the initial number of beers on the wall and returns the number of iterations needed to remove all the bottles, in addition to providing the number of bottles removed in the last iteration.
    """

    bottle_counter = 0
    while initial_bottles > 0:
        bottle_counter += 1
        if initial_bottles > bottle_counter:
            initial_bottles -= bottle_counter
        else:
            return f'Number of bottles removed in the last iteration: {initial_bottles} Number of iterations: {bottle_counter}'

if __name__ == "__main__":
    print(beer(99))