def diamond(width):
    """Text diamond maker.
    
    Create diamond with amazing か character of any size you want. Version 2.1.
    """
    try:
        if width % 2 == 0:
            print("Width needs to be odd!")
            return
    except TypeError:
        print('Width needs to be a number!')
        return
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
        
diamond(9)
diamond("LOL")
diamond(4)
diamond(21)