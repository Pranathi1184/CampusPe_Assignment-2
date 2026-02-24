# Q2: Simple Calculator

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nResults:")

    # Addition
    print(num1, "+", num2, "=", num1 + num2)

    # Subtraction
    print(num1, "-", num2, "=", num1 - num2)

    # Multiplication
    print(num1, "*", num2, "=", num1 * num2)

    # Division
    # checking division to avoid divide by zero error
    if num2 != 0:
        print(num1, "/", num2, "=", num1 / num2)
    else:
        print(num1, "/", num2, "= Cannot divide by zero")

    # Modulus
    if num2 != 0:
        print(num1, "%", num2, "=", num1 % num2)
    else:
        print(num1, "%", num2, "= Cannot find modulus")

    # Exponent
    print(num1, "^", num2, "=", num1 ** num2)

except:
    print("Please enter valid numbers!")