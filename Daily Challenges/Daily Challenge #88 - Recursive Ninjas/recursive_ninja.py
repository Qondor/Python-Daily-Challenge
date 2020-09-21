def ninja_chirp(total_chirp):
    """Ninjas frequently need to signal each other in code. They often employ natural sounds as cover. Our ninja will chirp like a bird, with different amounts of chirps signifying different messages.

    Function returns number of chirps given by user.
    """
    return "chirp" + ("-chirp" * (total_chirp - 1))

if __name__ == "__main__":
    print(ninja_chirp(1))