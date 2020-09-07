def setalarm(employed, vacation):
    """Function that determines whether alram is needed or not.

    The function should return true if you are employed and not on vacation (because these are the circumstances under which you need to set an alarm). It should return false otherwise.
    """
    if employed == True and vacation == False:
        return True
    else:
        return False

if __name__ == "__main__":
    print(setalarm(True, False))