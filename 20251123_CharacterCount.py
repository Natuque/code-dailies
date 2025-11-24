** start of main.py **

def count_characters(sentence):
    array = []

    # Change to lowercase and strip space
    sentence = sentence.lower().replace(" ","")
    
    # Add it into the array
    for char in sentence:
        if char.isalpha():
            array.append(char)

    # Sort
    array.sort()

    # Dictionary to start counting
    alphabets = {}

    for each in array:
        if each in alphabets:
            alphabets[each] += 1
        else: 
            alphabets[each] = 1

    # Final List to print
    finalList = []

    for key in alphabets:
        value = f"{key} {alphabets[key]}"
        finalList.append(value)

    print(finalList)
    return finalList

count_characters("hello world")
count_characters("I love coding challenges!")

** end of main.py **

