def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Yes")
                return "Yes"
            else:
                print("No")
                return "No"
        else:
            print("Yes")
            return "Yes"
    else:
        print("No")
        return "No"
