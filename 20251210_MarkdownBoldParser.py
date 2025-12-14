** start of main.py **

def parse_bold(markdown):
    # Using regex to extract
    #standard library
    import re

    # Regex Pattern
    # Pattern: 
    # Captures (** or __) 
    # -> (?!\s) for non whitespace, Negative lookahead
    # -> Captures text non-greedily 
    # -> (?<!\s) for no whitespace behind, Negative Look behind 
    # -> Matches the opening delimiter
    pattern = r"(\*\*|__)(?!\s)(.+?)(?<!\s)\1"

    # Substitution: <b> followed by the content of the second capturing group (\2) followed by </b>. The first group (\1) is discarded.
    replacement = r"<b>\2</b>"

    # Final using replace
    final = re.sub(pattern, replacement, markdown)

    print(final)
    return final

parse_bold("**This is bold**")
parse_bold("__This is also bold__")
parse_bold("**This is not bold **")
parse_bold("__ This is also not bold__")
parse_bold("The **quick** brown fox __jumps__ over the **lazy** dog.")

** end of main.py **

