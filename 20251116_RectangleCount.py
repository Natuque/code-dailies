def count_rectangles(width, height):
    # Formula for rectangle count
    # total = (width(width+1)/2) * (width(width+1)/2)
    width_Total = (width * (width + 1)) / 2
    height_Total = (height * (height + 1)) / 2

    rectangles_Total = width_Total * height_Total

    return rectangles_Total



count_rectangles(2,3)

