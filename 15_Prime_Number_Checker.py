# Q15: Prime Number Checker

try:
    num = int(input("Enter a number: "))

    # PART 1: Single number check
    if num < 0:
        print(num, "is NOT a prime number (negative numbers are not prime).")

    elif num == 0 or num == 1:
        print(num, "is NOT a prime number.")

    elif num == 2:
        print("2 is a PRIME number.")

    else:
        divisor = 2
        is_prime = True

        # checking divisibility from 2 to num-1
        while divisor < num and is_prime:
            if num % divisor == 0:
                is_prime = False
            divisor = divisor + 1

        if is_prime:
            print(num, "is a PRIME number.")
        else:
            print(num, "is NOT a prime number.")

    # PART 2: Range primes
    start = int(input("\nEnter start range: "))
    end = int(input("Enter end range: "))

    print("Prime numbers:")

    number = start

    while number <= end:

        if number >= 2:

            divisor = 2
            prime_flag = True

            while divisor < number and prime_flag:
                if number % divisor == 0:
                    prime_flag = False
                divisor = divisor + 1

            if prime_flag:
                print(number)

        number = number + 1

except:
    print("Please enter valid integers!")