** start of main.py **

def compress_string(sentence):
    # Importing Counter 
    from collections import Counter

    count = Counter(sentence.split(" "))

    finalString = ""

    for each in count:
        # Add space if its not the first word
        if finalString != "":
            finalString += " "

        if count[each] > 1:
            finalString += f"{each}({count[each]})"
        else:
            finalString += each

    print(finalString)
    return finalString

compress_string("yes yes yes please")
compress_string("I have have have apples")
compress_string("one one three and to the the the the")
compress_string("route route route route route route tee tee tee tee tee tee")

    

** end of main.py **

