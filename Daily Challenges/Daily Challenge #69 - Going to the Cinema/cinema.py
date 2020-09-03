def movie(card, ticket, perc):
    """Cinema ticket discount calculator.

    Calculates after how many bought tickets it's worth to buy cinema discount card.
    """
    normal_price = 0
    card_price = card
    iteration = 0
    while normal_price < card_price:
        iteration += 1
        normal_price += ticket
        card_price += ticket * (perc**iteration)

    return iteration


if __name__ == "__main__":
    print(movie(500, 15, 0.9))