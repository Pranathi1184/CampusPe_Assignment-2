# Q11: Number Pattern Printer

print("Choose Pattern:")
print("1. Pattern 1")
print("2. Pattern 2")
print("3. Pattern 3")
print("4. Pattern 4")

choice = input("Enter pattern number: ")

if choice <= "4" and choice >= "1":
    height = int(input("Enter height: "))

print()


# Pattern 1
if choice == "1":
    for i in range(1, height + 1):
        line = ""
        for j in range(1, i + 1):
            line = line + str(j) + " "
        print(line)

# Pattern 2
elif choice == "2":
    for i in range(1, height + 1):
        line = ""
        for j in range(1, i + 1):
            line = line + str(i) + " "
        print(line)

# Pattern 3
elif choice == "3":
    for i in range(height, 0, -1):
        line = ""
        for j in range(i, 0, -1):
            line = line + str(j) + " "
        print(line)

# Pattern 4
elif choice == "4":
    for i in range(1, height + 1):
        line = ""

        for j in range(1, i + 1):
            line = line + str(j)

        for j in range(i - 1, 0, -1):
            line = line + str(j)

        print(line)

else:
    print("Invalid choice")