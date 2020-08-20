def card_shuffler(cards):
    """Automatic card shuffler.

    More in .txt file.
    """
    if len(cards) % 2 != 0:
        return "Cards in the stack should be even"
    first_iteration = 0
    second_iteration = int(len(cards)/2)
    result = []

    while first_iteration < len(cards)/2:
        result.append(cards[first_iteration])
        result.append(cards[second_iteration])
        first_iteration += 1
        second_iteration += 1
    
    return result


if __name__ == "__main__":
    print(card_shuffler(['ace', 'two', 'three', 'four', 'five', 'six', 'king', 'queen']))