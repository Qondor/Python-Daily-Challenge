def pile(total_cubes):
    biggest_layer = 0
    all_layers = 0
    n = 1
    while all_layers < total_cubes:
        all_layers += n**3
        n += 1
    if all_layers == total_cubes:
        return n - 1
    else:
        return 0

if __name__ == "__main__":
    print(pile(1071225))