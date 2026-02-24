# Q14: Factorial Calculator

try:
    num = int(input("Enter a number: "))

    if num < 0:
        print("Factorial is not defined for negative numbers.")

    elif num == 0:
        print("0! = 1")

    else:
        factorial = 1
        steps = ""   # to store step-by-step string

        for i in range(num, 0, -1):
            factorial = factorial * i

            steps = steps + str(i)

            if i != 1:
                steps = steps + " x "

        print(str(num) + "! = " + steps + " = " + str(factorial))

except:
    print("Please enter a valid number!")