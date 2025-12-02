** start of main.py **

def is_valid_message(message, validation):
    message = message.lower()
    validation = validation.lower()
    words = message.split(" ")

    firstLetter = ""

    for each in words:
        firstLetter += each[0]

    if firstLetter == validation:
        print("True")
        return True
    else:
        print("False")
        return False


is_valid_message("hello world", "hw")
is_valid_message("ALL CAPITAL LETTERS", "acl")
is_valid_message("Coding challenge are boring.", "cca")

** end of main.py **

