** start of main.py **

def one_hundred(chars):
    finalChar = ""

    while len(finalChar) < 100:
        finalChar += chars
    
    finalChar = finalChar[0:100]

    print(finalChar)
    return finalChar

one_hundred("One hundred ")
one_hundred("freeCodeCamp ")

** end of main.py **

