# Q17: Palindrome Checker

text = input("Enter word/number: ")

print("Original:", text)

lower_text = text.lower()

length = len(text)

reversed_text = ""
i = length - 1

while i >= 0:
    reversed_text = reversed_text + text[i]
    i = i - 1

print("Reversed:", reversed_text)

# checking palindrome step by step
left = 0
right = length - 1
is_palindrome = True

while left < right:

    print("Comparing:", lower_text[left], "and", lower_text[right])

    if lower_text[left] != lower_text[right]:
        is_palindrome = False

    left = left + 1
    right = right - 1

# final result
if is_palindrome:
    print("Result: PALINDROME")
else:
    print("Result: NOT PALINDROME")