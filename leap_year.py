def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True  # Divisible by 400, so leap year
            else:
                return False  # Divisible by 100 but not by 400, not a leap year
        else:
            return True  # Divisible by 4 but not by 100, so leap year
    else:
        return False  # Not divisible by 4, not a leap year


print(leap_year(2100))