# Q7: Temperature Converter

loop=True
while loop:
    print("\n===== TEMPERATURE CONVERTER =====")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

    choice = input("Enter your choice: ")
    
    if choice < "7" and choice > "0":
        temperature = float(input("Enter temperature value: "))

    if choice == "1":
        result = (temperature * 9/5) + 32
        print("Result:", result, "°F")

    elif choice == "2":
        result = (temperature - 32) * 5/9
        print("Result:", result, "°C")

    elif choice == "3":
        result = temperature + 273.15
        print("Result:", result, "K")

    elif choice == "4":
        result = temperature - 273.15
        print("Result:", result, "°C")

    elif choice == "5":
        result = (temperature - 32) * 5/9 + 273.15
        print("Result:", result, "K")

    elif choice == "6":
        result = (temperature - 273.15) * 9/5 + 32
        print("Result:", result, "°F")
            
    elif choice == "7":
        print("Exiting Temperature Converter.")
        loop=False

    else:
        print("Invalid choice. Please select 1 to 7.")
