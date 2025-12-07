** start of main.py **

def format_date(date_string):
    # Clean the string cause datetime is having trouble with nonleading date
    month = date_string.split(" ")[0]
    date = date_string.split(" ")[1].strip(",")
    date = "0" + date if len(date) == 1 else date
    year = date_string.split(" ")[2]

    # Using datetime module from standard library
    from datetime import datetime

    # Making the date object for the month only
    monthObj = str(datetime.strptime(month, "%B").month)

    # Pad the month like the date
    month = "0" + monthObj if len(monthObj) == 1 else monthObj

    # Make the final date format
    finalDate = f"{year}-{month}-{date}"

    print(finalDate)
    return(finalDate)


format_date("December 6, 2025")
format_date("January 1, 2000")
format_date("November 11, 1111")
format_date("September 7, 512")
format_date("May 4, 1950")
format_date("February 29, 1992")

** end of main.py **

