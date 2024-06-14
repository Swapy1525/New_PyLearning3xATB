# Leap year checker

year = int(input("Enter the year\n"))

if year % 4 == 0 and year % 400 == 0:
    print(year, "is a Leap Year")
elif year % 100!= 0:
    print(year, "not a Leap year")


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


year = int(input("enter year"))

if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
