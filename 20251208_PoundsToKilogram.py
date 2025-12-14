** start of main.py **

def convert_to_kgs(lbs):
    # Get kilogram value
    # This is a string formatter with a format specifier through :, lots of format specifiers available
    kilo = f"{round(lbs * 0.453592, 2):.2f}"

    # Gonna use list splicing to remove s as last index
    pnd = "pounds"
    kg = "kilograms"

    # Final String
    finalString = f"{lbs} {pnd if lbs != 1 else pnd[:-1]} equals {kilo} {kg if float(kilo) != 1 else kg[:-1]}."

    print(finalString)
    return finalString

convert_to_kgs(1)
convert_to_kgs(0)
convert_to_kgs(100)
convert_to_kgs(2.5)
convert_to_kgs(2.20462)

** end of main.py **

