# Q9: Ticket Pricing System

try:
    tickets = int(input("Enter number of tickets: "))
    day = input("Enter day of the week: ").lower()

    total_base = 0

    # loop for each person
    for i in range(1, tickets + 1):
        age = int(input("Enter age for person " + str(i) + ": "))

        if age < 3:
            price = 0
            print("Person", i, ": Free ticket")
        elif age >= 3 and age <= 12:
            price = 150
            print("Person", i, ": Child ticket = ₹150")
        elif age >= 13 and age <= 59:
            price = 300
            print("Person", i, ": Adult ticket = ₹300")
        else:
            price = 200
            print("Person", i, ": Senior ticket = ₹200")

        total_base = total_base + price

    print("\nTotal base price:", total_base)

    # Day discount
    discount_percent = 0

    if day == "friday" or day == "saturday" or day == "sunday":
        discount_percent = 20

    discount_amount = total_base * discount_percent / 100
    final_price = total_base - discount_amount

    print("Discount:", discount_percent, "%")
    print("Price after discount:", final_price)
    print("Total amount:", final_price)

except:
    print("Please enter valid inputs!")