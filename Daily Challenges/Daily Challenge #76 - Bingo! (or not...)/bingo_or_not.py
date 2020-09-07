def bingo(numbers):
    """For this game of BINGO, you will receive a single array of 10 numbers from 1 to 26 as an input. Duplicate numbers within the array are possible.

    Function where you will win the game if your numbers can spell "BINGO".
    """
    bingo_set = set([2, 9, 14, 7, 15])
    if bingo_set.issubset(set(numbers)):
        return "WIN"
    else:
        return "LOSE"
if __name__ == "__main__":
    print(bingo([21,13,2,7,5,14,7,15,9,10]))