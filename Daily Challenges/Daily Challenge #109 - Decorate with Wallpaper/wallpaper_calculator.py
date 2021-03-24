import math
import inflect

p = inflect.engine()

def wallpaper(l, w, h):
    """How much wallpaper do I need?

    Function calculates and return a plain English word in lower case the number of rolls that should be purchased, with 15% extra to be sure.
    """

    roll_area = 5.2
    room_area = l*w*h
    rolls = 1.15*(room_area)/roll_area
    return f'{p.number_to_words(math.ceil(rolls))}'

if __name__ == "__main__":
    print(wallpaper(6.3, 4.5, 3.29))