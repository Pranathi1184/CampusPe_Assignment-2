# Q6: Grade Calculator

try:
    maths = float(input("Enter marks for Maths (out of 100): "))
    science = float(input("Enter marks for Science (out of 100): "))
    english = float(input("Enter marks for English (out of 100): "))
    social = float(input("Enter marks for Social (out of 100): "))
    computer = float(input("Enter marks for Computer (out of 100): "))

    print("\nMarks Entered:")
    print("Maths:", maths)
    print("Science:", science)
    print("English:", english)
    print("Social:", social)
    print("Computer:", computer)

    # calculating total and percentage
    total = maths + science + english + social + computer
    percentage = total / 5

    print("\nTotal Marks:", total, "/ 500")
    print("Percentage:", percentage)

    # Grade calculation
    if percentage >= 90:
        grade = "A+ (Outstanding)"
    elif percentage >= 80:
        grade = "A (Excellent)"
    elif percentage >= 70:
        grade = "B (Good)"
    elif percentage >= 60:
        grade = "C (Average)"
    elif percentage >= 50:
        grade = "D (Pass)"
    else:
        grade = "F (Fail)"

    print("Grade:", grade)

    # Pass condition: all subjects must be >= 40
    if maths >= 40 and science >= 40 and english >= 40 and social >= 40 and computer >= 40:
        print("Result: Pass")
    else:
        print("Result: Fail")

except:
    print("Please enter valid numeric marks!")