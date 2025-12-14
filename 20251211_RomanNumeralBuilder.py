** start of main.py **

def to_roman(num):
    roman_map = [
        # Tuples for ordering purposes
        (1000, "M"),
        (900, "CM"),  # Handles 900
        (500, "D"),
        (400, "CD"),  # Handles 400
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]  

    romanFinal = ""

    # Iterate through the properly ordered list
    for value, symbol in roman_map:
    # Use a while loop to repeatedly subtract the largest possible value
        while num >= value:
            romanFinal += symbol
            num -= value


    print(romanFinal)
    return romanFinal

to_roman(18)
to_roman(19)
to_roman(1464)
to_roman(2025)
to_roman(3999)

** end of main.py **

