# Q4: Age Calculator

CURRENT_YEAR = 2026
CURRENT_MONTH = 2
CURRENT_DAY = 24

try:
    birth_year = int(input("Enter your birth year: "))
    birth_month = int(input("Enter your birth month (1-12): "))
    birth_day = int(input("Enter your birth day (1-31): "))

    # basic validation
    if birth_year > CURRENT_YEAR:
        print("Birth year cannot be in the future!")

    elif birth_month < 1 or birth_month > 12:
        print("Invalid birth month!")

    elif birth_day < 1 or birth_day > 31:
        print("Invalid birth day!")

    else:
        age = CURRENT_YEAR - birth_year

        # adjusting age if birthday hasn't occurred yet this year
        if birth_month > CURRENT_MONTH:
            age = age - 1
        elif birth_month == CURRENT_MONTH:
            if birth_day > CURRENT_DAY:
                age = age - 1

        print("\nCurrent age:", age)
        print("Age in months:", age * 12)
        print("Age in days:", age * 365)
        print("Age in hours:", age * 365 * 24)
        print("Age in minutes:", age * 365 * 24 * 60)
        print("Years until age 100:", 100 - age)

except:
    print("Please enter valid numeric values!")