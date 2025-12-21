** start of main.py **

def has_consonant_count(text, target):
    # Using Regex to isolate
    import re

    # Removing All vowels
    removeVowel = r"[AEIOUaeiou]"
    noVowel = re.sub(removeVowel, "", text)

    # Retain only Alphabets
    maintainAlphabets = r"[^A-Za-z]"
    finalString = re.sub(maintainAlphabets,"", noVowel)

    # Check
    if len(finalString) == target:
        print("True")
        return True
    else:
        print("False")
        return False

has_consonant_count("helloworld", 7)
has_consonant_count("eieio", 5)
has_consonant_count("freeCodeCamp Rocks!", 11)
has_consonant_count("Th3 Qu!ck Br0wn F0x Jump5 0ver Th3 L@zy D0g.", 24)
has_consonant_count("Th3 Qu!ck Br0wn F0x Jump5 0ver Th3 L@zy D0g.", 23)

** end of main.py **

