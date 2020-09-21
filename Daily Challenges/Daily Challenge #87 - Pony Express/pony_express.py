def stations(distances):
    """Pony express riders function.

    Return how many riders it would take to get from point A to point B. Riders will never agree to riding more than 100 miles.
    """
    total_distance = sum(distances)
    if total_distance <= 100:
        return "1 rider"
    elif total_distance % 100 != 0:
        return f"{int(total_distance / 100 + 1)} riders"
    else:
        return f"{int(total_distance / 100)} riders"
    return total_distance
if __name__ == "__main__":
    print(stations([43, 23, 40, 13]))