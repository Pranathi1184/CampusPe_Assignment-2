# Q5: Bill Splitter

try:
    total_bill = float(input("Enter total bill: "))
    people = int(input("Number of people: "))
    tax_percent = float(input("Tax percentage: "))
    tip_percent = float(input("Tip percentage: "))

    if people <= 0:
        print("Number of people must be at least 1")

    else:
        tax_amount = total_bill * tax_percent / 100
        after_tax = total_bill + tax_amount
        tip_amount = after_tax * tip_percent / 100
        final_total = after_tax + tip_amount
        per_person = final_total / people

        print("\n=== BILL BREAKDOWN ===")
        print("Subtotal:   ₹", total_bill)
        print("Tax (" + str(tax_percent) + "%):   ₹", tax_amount)
        print("After tax:  ₹", after_tax)
        print("Tip (" + str(tip_percent) + "%):   ₹", tip_amount)
        print("Total:      ₹", final_total)
        print("Per person: ₹", per_person)

except:
    print("Please enter valid numeric values!")