def diamond(width):
    """Text diamond maker.
    
    Create diamond with amazing か character of any size you want. Version 2.1.
    """
    try:
        if width % 2 == 0:
            return "Width needs to be odd!"
            
    except TypeError:
        return "Width needs to be a number!"

    width += 1
    x_pos = (width//2 - 1)
    y_pos = range(width)
    for star_count in y_pos:
        if star_count % 2 == 1:
                print("  " * x_pos + "か" * star_count)
                x_pos -= 1
    x_pos = 1
    for star_count in reversed(y_pos):   
        if star_count != (width - 1) and star_count % 2 == 1:
            print("  " * x_pos + "か" * star_count)
            x_pos += 1

if __name__ == "__main__":
    print(diamond(9))
    print(diamond("LOL"))
    print(diamond(4))
    print(diamond(21))