** start of main.py **

def pairwise(arr, target):
    mapped = {}

    for index, value in enumerate(arr):
        mapped[value] = index
    
    seen = {}
    finalTotal = 0

    for each in mapped:
        potentialPair = target - each

        if potentialPair not in seen:
            seen[each] = mapped[each]
        else:
            finalTotal += mapped[each] + mapped[potentialPair]
            # Remove from seen to prevent duplicates
            del seen[potentialPair]

    return finalTotal

pairwise([2, 3, 4, 6, 8], 10)
pairwise([4, 1, 5, 2, 6, 3], 7)
pairwise([-30, -15, 5, 10, 15, -5, 20, -40], -20)
pairwise([-30, -15, 5, 10, 15, -5, 20, -40], -20)

** end of main.py **

