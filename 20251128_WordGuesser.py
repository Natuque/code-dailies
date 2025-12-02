** start of main.py **

def compare(word, guess):
    word = word.upper()
    guess = guess.upper()
    # Check if there's repeating letters in the word
    # Using a set cause a set only accepts unique values
    count = {}

    for char in word:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    
    finalWord = list(guess)
    indexCount = list(range(0, len(word)))
    zipped = list(zip(word,guess))

    for index in indexCount:
        if finalWord[index] == word[index]:
            if count[finalWord[index]] > 0:
                count[finalWord[index]] -= 1
                finalWord[index] = "2"
    for index in indexCount:
        if finalWord[index] == "2":
            pass
        elif finalWord[index] != word[index] and finalWord[index] in count:
            if count[finalWord[index]] > 0:
                count[finalWord[index]] -= 1
                finalWord[index] = "1"
            else:
                finalWord[index] = "0"
        else:
            finalWord[index] = "0"
    
    finalWord = "".join(finalWord)

    print(finalWord)
    return finalWord



compare("APPLE", "POPPA")
compare("REACT", "TRACE")
compare("DEBUGS", "PYTHON")
compare("JAVASCRIPT", "TYPESCRIPT")


** end of main.py **

