** start of main.py **

def title_case(title):
    title = " ".join([each.capitalize() for each in title.split(" ")])

    print(title)
    return title

title_case("hello world")
title_case("the quick brown fox")
title_case("JAVASCRIPT AND PYTHON")
title_case("AvOcAdO tOAst fOr brEAkfAst")

** end of main.py **

