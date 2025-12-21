** start of main.py **

def purge_most_frequent(arr):
    # Using a python library to count efficiently
    from collections import Counter
    count = Counter(arr)
    maxAmount = count.most_common(1)[0][1]

    # Targets to remove
    removeList = [val for val, freq in count.items() if freq == maxAmount]

    arr = [purge for purge in arr if purge not in removeList]

    print(arr)
    return arr

purge_most_frequent([1, 2, 2, 3])
purge_most_frequent(["a", "b", "d", "b", "c", "d", "c", "d", "c", "d"])
purge_most_frequent(["red", "blue", "green", "red", "blue", "green", "blue"])
purge_most_frequent([5, 5, 5, 5])

** end of main.py **

