# Q10: ATM Simulator with History

balance = 10000
loop = True
history = ""   # store transaction history as text

while loop:

    print("\nATM SIMULATOR")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Transaction History")
    print("5. Exit")

    choice = input("Enter choice: ")

    # Check balance
    if choice == "1":
        print("Current balance: ₹", balance)


    # Deposit
    elif choice == "2":
        try:
            amount = int(input("Enter amount to deposit: "))

            if amount > 0:
                balance = balance + amount
                print("Deposit successful!")
                print("New balance: ₹", balance)

                history = history + "Deposited ₹" + str(amount) + "\n"

            else:
                print("Enter valid amount!")

        except:
            print("Invalid input!")

    # Withdraw
    elif choice == "3":
        try:
            amount = int(input("Enter amount to withdraw: "))

            if amount <= 0:
                print("Enter valid amount!")

            elif amount > balance:
                print("Insufficient balance!")

            elif balance - amount < 500:
                print("Minimum balance ₹500 must remain!")

            else:
                balance = balance - amount
                print("Withdrawal successful!")
                print("New balance: ₹", balance)

                history = history + "Withdrew ₹" + str(amount) + "\n"

        except:
            print("Invalid input!")

    
    # View history
    elif choice == "4":
        print("\nTransaction History:")
        if history == "":
            print("No transactions yet.")
        else:
            print(history)
    
    # Exit
    elif choice == "5":
        print("Thank you for using ATM.")
        loop = False

    else:
        print("Invalid choice!")
