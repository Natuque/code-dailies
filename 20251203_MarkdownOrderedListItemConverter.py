** start of main.py **

def convert_list_item(markdown):
    markdown = markdown.strip()

    # Check for number eligibility
    if not markdown[0].isdigit():
        print("Invalid format")
        return "Invalid format"
    elif not markdown[1] == ".":
        print("Invalid format")
        return "Invalid format"
    
    # Get the proper text
    markdown = f"<li>{markdown[2:].strip()}</li>"

    print(markdown)
    return markdown


convert_list_item("1. My item") 
convert_list_item(" 1.  Another item")
convert_list_item("1 . invalid item")
convert_list_item("2. list item text")
convert_list_item(". invalid again")
convert_list_item("A. last invalid")

** end of main.py **

