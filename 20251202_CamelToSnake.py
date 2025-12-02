** start of main.py **

def to_snake(camel):
    newString = ""

    for i in camel:
        if not i.isupper():
            newString += i
        else:
            newString += f"_{i.lower()}"

    print(newString)
    return newString

to_snake("helloWorld")
to_snake("myVariableName")

** end of main.py **

