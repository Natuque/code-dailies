** start of main.py **

# Added Type hinting for practice
def speed_check(speed_mph: int, speed_limit_kph: int) -> str:
    # Convert
    miles_in_KM = round(speed_mph * 1.60934)
    if miles_in_KM <= speed_limit_kph:
        print("Not Speeding")
        return "Not Speeding"
    elif (speed_limit_kph + 5) >= miles_in_KM > speed_limit_kph :
        print("Warning")
        return "Warning"
    elif miles_in_KM > (speed_limit_kph + 5):
        print("Ticket")
        return "Ticket"


speed_check(30, 70)
speed_check(40, 60)
speed_check(40, 65)
speed_check(60, 90)
speed_check(65, 100)
speed_check(88, 40)

** end of main.py **

