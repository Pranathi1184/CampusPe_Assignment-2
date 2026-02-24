# Q13: Sum and Average Calculator with Bonus (No lists used)

try:
    count = int(input("How many numbers? "))

    if count <= 0:
        print("Enter a positive count!")

    else:
        numbers_text = ""   # storing numbers as text
        total = 0

        i = 1
        while i <= count:
            num = int(input("Enter number " + str(i) + ": "))
            total = total + num
            numbers_text = numbers_text + str(num) + " "
            i = i + 1

        average = total / count

        # Find max and min
        i = 0
        current = ""
        maximum = None
        minimum = None

        while i < len(numbers_text):
            if numbers_text[i] != " ":
                current = current + numbers_text[i]
            else:
                value = int(current)

                if maximum is None or value > maximum:
                    maximum = value

                if minimum is None or value < minimum:
                    minimum = value

                current = ""
            i = i + 1

        # Sorting manually
        # Convert string into array-like structure using simple indexing
        arr = [0] * count
        index = 0
        current = ""

        for ch in numbers_text:
            if ch != " ":
                current = current + ch
            else:
                arr[index] = int(current)
                current = ""
                index = index + 1

        i = 0
        while i < count:
            j = i + 1
            while j < count:
                if arr[i] > arr[j]:
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp
                j = j + 1
            i = i + 1

        # Median
        if count % 2 == 1:
            median = arr[count // 2]
        else:
            median = (arr[count // 2 - 1] + arr[count // 2]) / 2

        # Mode
        max_count = 0
        mode = arr[0]

        i = 0
        while i < count:
            current_count = 0
            j = 0

            while j < count:
                if arr[i] == arr[j]:
                    current_count = current_count + 1
                j = j + 1

            if current_count > max_count:
                max_count = current_count
                mode = arr[i]

            i = i + 1

        # Output
        print("\nSum:", total)
        print("Average:", average)
        print("Maximum:", maximum)
        print("Minimum:", minimum)
        print("Median:", median)
        print("Mode:", mode)

except:
    print("Please enter valid numbers!")