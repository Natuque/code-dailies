** start of main.py **

def difference(arr1, arr2):
    # List Comprehension I suppose?
    list1 = [value for value in arr1 if value not in arr2]
    list2 = [value for value in arr2 if value not in arr1]

    finalList = list1 + list2

    print(finalList)
    return finalList

def betterDifference(arr1, arr2):
    # Gemini says the more pythonic way of doing this is through sets like this
    # Cause using list comprehension eats time

    # First you convert everything to set
    list1 = set(arr1)
    list2 = set(arr2)

    # ^ is for symmetric difference
    finalList = list(list1 ^ list2)

    print(finalList)
    return finalList


difference([1, 2, 3], [3, 4, 5])
betterDifference([1, 2, 3], [3, 4, 5])
difference(["a", "b"], ["c", "b"])
difference([1, "a", 2], [2, "b", "a"])
difference([1, 3, 5, 7, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9])

** end of main.py **

