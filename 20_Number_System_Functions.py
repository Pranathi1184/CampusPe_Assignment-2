# Q20: Number System Functions

# 1. factorial
def factorial(n):
    if n < 0:
        print("Factorial not defined for negative numbers")
        return

    result = 1
    i = 1

    # multiplying numbers from 1 to n
    while i <= n:
        result = result * i
        i = i + 1

    print("Factorial:", result)


# 2. prime check
def is_prime(n):
    if n < 2:
        print("Not prime")
        return

    divisor = 2
    prime_flag = True

    # checking divisibility manually
    while divisor < n and prime_flag:
        if n % divisor == 0:
            prime_flag = False
        divisor = divisor + 1

    if prime_flag:
        print("Prime number")
    else:
        print("Not prime")


# 3. fibonacci
def fibonacci(n):
    if n <= 0:
        print("Invalid position")
        return

    a = 0
    b = 1
    count = 1

    while count < n:
        temp = a + b
        a = b
        b = temp
        count = count + 1

    print("Fibonacci number:", b)


# 4. sum of digits
def sum_of_digits(n):
    if n < 0:
        n = n * -1

    total = 0

    while n > 0:
        digit = n % 10
        total = total + digit
        n = n // 10

    print("Sum of digits:", total)


# 5. reverse number
def reverse_number(n):
    rev = 0

    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10

    print("Reversed number:", rev)


# 6. armstrong number
def is_armstrong(n):
    temp = n
    total = 0

    while temp > 0:
        digit = temp % 10
        total = total + (digit * digit * digit)
        temp = temp // 10

    if total == n:
        print("Armstrong number")
    else:
        print("Not Armstrong")


# 7. gcd
def gcd(a, b):
    i = 1
    gcd_value = 1

    while i <= a and i <= b:
        if a % i == 0 and b % i == 0:
            gcd_value = i
        i = i + 1

    print("GCD:", gcd_value)


# 8. lcm
def lcm(a, b):
    greater = a
    if b > a:
        greater = b

    lcm_value = greater

    while True:
        if lcm_value % a == 0 and lcm_value % b == 0:
            print("LCM:", lcm_value)
            break

        lcm_value = lcm_value + greater


# 9. perfect number
def is_perfect_number(n):
    i = 1
    total = 0

    while i < n:
        if n % i == 0:
            total = total + i
        i = i + 1

    if total == n:
        print("Perfect number")
    else:
        print("Not a perfect number")


# 10. menu
def math_menu():

    loop = True

    while loop:

        print("\nMATH FUNCTIONS MENU")
        print("1. Factorial")
        print("2. Prime check")
        print("3. Fibonacci")
        print("4. Sum of digits")
        print("5. Reverse number")
        print("6. Armstrong")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect number")
        print("10. Exit")

        choice = input("Enter choice: ")

        if choice == "10":
            loop = False

        elif choice == "1":
            n = int(input("Enter number: "))
            factorial(n)

        elif choice == "2":
            n = int(input("Enter number: "))
            is_prime(n)

        elif choice == "3":
            n = int(input("Enter position: "))
            fibonacci(n)

        elif choice == "4":
            n = int(input("Enter number: "))
            sum_of_digits(n)

        elif choice == "5":
            n = int(input("Enter number: "))
            reverse_number(n)

        elif choice == "6":
            n = int(input("Enter number: "))
            is_armstrong(n)

        elif choice == "7":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            gcd(a, b)

        elif choice == "8":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            lcm(a, b)

        elif choice == "9":
            n = int(input("Enter number: "))
            is_perfect_number(n)

        else:
            print("Invalid choice")


# start program
math_menu()