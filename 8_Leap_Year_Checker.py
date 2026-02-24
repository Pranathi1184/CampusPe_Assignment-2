# Q8: Leap Year Checker

try:
    year = int(input("Enter a year: "))

    # First condition: must be divisible by 4
    if year % 4 == 0:

        # Apply second condition
        if year % 100 != 0 or year % 400 == 0:
            print(year, "is a Leap Year.")

            # Reason messages
            if year % 100 != 0:
                print("Reason: It is divisible by 4 and not divisible by 100.")
            else:
                print("Reason: It is divisible by 4 and 400.")

        else:
            print(year, "is NOT a Leap Year.")
            print("Reason: It is divisible by 100 but not divisible by 400.")

    else:
        print(year, "is NOT a Leap Year.")
        print("Reason: It is not divisible by 4.")

except:
    print("Please enter a valid year!")