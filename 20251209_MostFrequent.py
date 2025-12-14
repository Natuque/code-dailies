** start of main.py **

def most_frequent(arr):
    from collections import Counter

    count = Counter(arr)

    # Counter has a most frequent check built in
    final = count.most_common(1)[0][0]

    print(final)
    return final


most_frequent(["a", "b", "a", "c"])
most_frequent([2, 3, 5, 2, 6, 3, 2, 7, 2, 9])
most_frequent([True, False, "False", "True", False])
most_frequent([40, 20, 70, 30, 10, 40, 10, 50, 40, 60])

** end of main.py **

