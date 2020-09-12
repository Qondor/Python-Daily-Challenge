def third_angle(first_angle, second_angle):
    """You are given two angles of a triangle in degrees.

    Write a function to return the third angle. Only positive integers will be tested.
    """
    if first_angle == 0 or second_angle == 0:
        return "Not a triangle."
    else:
        return 180 - (first_angle + second_angle)
if __name__ == "__main__":
    print(third_angle(10, 20))