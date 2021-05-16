def middle(X, Y, N):
    """Function that will take a key of X and place it in the middle of Y repeated N times.

    If X cannot be placed in the middle, return X.
N will always be > 0.
    """
    if N % 2 != 0:
        return X
    else:
        return (int(N/2) * Y) + X + (int(N/2) * Y)

if __name__ == "__main__":
    print(middle("-_-", "@", 26))