def deodorant(content, evap_per_day, threshold):
    """This program tests the life of an evaporator containing a gas.

    We know the content of the evaporator (content in ml), the percentage of foam or gas lost every day (evap_per_day) and the threshold (threshold) in percentage beyond which the evaporator is no longer useful. All numbers are strictly positive.

    The program reports the nth day (as an integer) on which the evaporator will be out of use.
    """
    out_of_use = 0
    while content > threshold:
        content -= content * (evap_per_day / 100)
        out_of_use += 1
    return out_of_use

if __name__ == "__main__":
    print(deodorant(500, 10, 50))