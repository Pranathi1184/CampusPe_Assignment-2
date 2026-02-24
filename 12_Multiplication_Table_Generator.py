# Q12: Multiplication Table Generator

print("1. Table for a number")
print("2. Full tables from 1 to 10 ")

choice = input("Enter choice: ")

# Option 1: Normal table
if choice == "1":
    try:
        number = int(input("Enter number: "))
        end = int(input("Enter range (end): "))

        if end <= 0:
            print("Range must be positive!")

        else:
            print("\nMultiplication Table of", number)

            for i in range(1, end + 1):
                result = number * i
                print(number, "x", i, "=", result)

    except:
        print("Please enter valid numbers!")

# Option 2: Bonus full tables
elif choice == "2":
    print("\nFull Multiplication Table (1 to 10)\n")

    for i in range(1, 11):   # row multiplier

        line = ""

        for j in range(1, 11):   # column number
            result = j * i

            cell = str(j) + "*" + str(i) + "=" + str(result)

            # make all cells same width
            space_needed = 10 - len(cell)
            cell = cell + " " * space_needed

            line = line + cell

        print(line)

else:
    print("Invalid choice")