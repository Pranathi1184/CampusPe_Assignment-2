# Q3: String Manipulator

# taking sentence input
text = input("Enter a sentence: ")

print("Original:", text)

# Count characters
char_count = len(text)

# Count characters without spaces
char_no_space = 0
for ch in text:
    if ch != " ":
        char_no_space = char_no_space + 1

# Count words 
word_count = 0
in_word = False

for ch in text:
    if ch != " " and in_word == False:
        word_count = word_count + 1
        in_word = True
    elif ch == " ":
        in_word = False

upper_text = text.upper()
lower_text = text.lower()

# Title Case
title_text = ""
new_word = True

for ch in lower_text:
    if ch == " ":
        title_text = title_text + " "
        new_word = True
    else:
        if new_word == True:
            title_text = title_text + ch.upper()
            new_word = False
        else:
            title_text = title_text + ch

# First word
first_word = ""
for ch in text:
    if ch == " ":
        break
    first_word = first_word + ch

# Last word
last_word = ""
temp = ""

for ch in text + " ":
    if ch != " ":
        temp = temp + ch
    else:
        if temp != "":
            last_word = temp
        temp = ""

# Reverse sentence using len and indexing
reversed_text = ""
i = len(text) - 1

while i >= 0:
    reversed_text = reversed_text + text[i]
    i = i - 1

print("Characters (with spaces):", char_count)
print("Characters (without spaces):", char_no_space)
print("Words:", word_count)
print("UPPERCASE:", upper_text)
print("lowercase:", lower_text)
print("Title Case:", title_text)
print("First word:", first_word)
print("Last word:", last_word)
print("Reversed:", reversed_text)