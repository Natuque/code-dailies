** start of main.py **

def count_permutations(s):
    # Standard Library: math cause it has factorial
    import math
    from collections import Counter

    # Length of characters in s
    length = len(s)

    # Counting character frequency
    # Counter makes a dictionary with counts for you
    count = Counter(s)

    # Calculate Total
    total = math.factorial(length)

    # Need to count the divide by cause unique character combos only
    base = 1
    for count in count.values():
        base *= math.factorial(count)

    # For final perms count its total / base
    final = total / base


    print(final)
    return final

count_permutations("abb")
count_permutations("abc")
count_permutations("racecar")
count_permutations("freecodecamp")

** end of main.py **

