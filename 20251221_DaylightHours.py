** start of main.py **

def daylight_hours(latitude):
    daylightTable = [
        (-90, 24),
        (-75, 23),
        (-60, 21),
        (-45, 15),
        (-30, 13),
        (-15, 12),
        (0, 12),
        (15, 11),
        (30, 10),
        (45, 9),
        (60, 6),
        (75, 2),
        (90, 0),
    ]

    # Takes the first element of the tuple, 
    # subtracts the target, 
    # and makes it positive (absolute value)

    # The key argument tells the min() function:
    # "Don't compare the items themselves. 
    # Instead, run every item through this 
    # function first, and compare the results of 
    # that function."

    # This method calculates the absolute difference
    # between your target and the first element of 
    # each tuple. The min() function then returns the
    # tuple that yielded the smallest difference.

    # Nearest latitude count

    nearestLat = min(daylightTable, key=lambda x: abs(x[0] - latitude))[1]

    print(nearestLat)
    return nearestLat

daylight_hours(45)
daylight_hours(0)
daylight_hours(-90)
daylight_hours(-10)
daylight_hours(23)
daylight_hours(88)
daylight_hours(-33)
daylight_hours(70)

** end of main.py **

