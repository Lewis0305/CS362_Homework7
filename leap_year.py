def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            pass
        else:
            return "Yes"
    else:
        return "No"