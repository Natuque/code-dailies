** start of main.py **

def parse_blockquote(markdown):
    # Use regex
    import re

    # Strip any whitespace
    markdown = markdown.strip()

    # Regex Pattern for removal
    pattern = r"^>\s*"

    # Remove the regex pattern
    markdown = re.sub(pattern, "", markdown)

    # Add the blockquotes
    markdown = f"<blockquote>{markdown}</blockquote>"

    print(markdown)
    return markdown


parse_blockquote("> This is a quote")
parse_blockquote(" > This is also a quote")
parse_blockquote("  >    So  Is  This")




** end of main.py **

