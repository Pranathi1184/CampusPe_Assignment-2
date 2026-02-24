# Q18: Calculator with Functions

# Basic operations
def add(a, b):
    return a + b
 

def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        print("Cannot divide by zero")
        return None
    return a / b


def modulus(a, b):
    if b == 0:
        print("Cannot do modulus by zero")
        return None
    return a % b


# power using loop instead of **
# works for positive integer powers
def power(a, b):
    return a**b


# BONUS: square root (simple check for perfect square)
def square_root(n):
    if n < 0:
        print("Square root not possible for negative numbers")
    else:
        i = 1
        found = False

        while i * i <= n:
            if i * i == n:
                print("Square root:", i)
                found = True
            i = i + 1

        if found == False:
            print("No exact square root found")


# BONUS: percentage
def percentage(a, b):
    if b == 0:
        print("Cannot divide by zero")
    else:
        result = (a / b) * 100
        print("Percentage:", result)


# main menu loop
def calculator():

    running = True

    while running:

        print("\nCALCULATOR MENU")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Square Root (Bonus)")
        print("8. Percentage (Bonus)")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == "9":
            running = False

        elif choice == "7":
            num = int(input("Enter number: "))
            square_root(num)

        elif choice == "8":
            a = int(input("Enter value: "))
            b = int(input("Enter total: "))
            percentage(a, b)

        elif choice in ["1", "2", "3", "4", "5", "6"]:

            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))

            if choice == "1":
                print("Result:", add(num1, num2))

            elif choice == "2":
                print("Result:", subtract(num1, num2))

            elif choice == "3":
                print("Result:", multiply(num1, num2))

            elif choice == "4":
                result = divide(num1, num2)
                if result != None:
                    print("Result:", result)

            elif choice == "5":
                result = modulus(num1, num2)
                if result != None:
                    print("Result:", result)

            elif choice == "6":
                print("Result:", power(num1, num2))

        else:
            print("Invalid choice")


calculator()