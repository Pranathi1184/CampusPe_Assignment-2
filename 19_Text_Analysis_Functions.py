# Q19: Text Analysis Functions

# count words
def count_words(text):
    count = 0
    in_word = False

    for ch in text:
        if ch != " " and in_word == False:
            count = count + 1
            in_word = True
        elif ch == " ":
            in_word = False

    return count


# count vowels
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for ch in text:
        if ch in vowels:
            count = count + 1

    return count


# count consonants
def count_consonants(text):
    vowels = "aeiouAEIOU"
    count = 0

    for ch in text:
        if ch != " " and ch not in vowels:
            count = count + 1

    return count


# reverse text
def reverse_text(text):
    i = len(text) - 1
    rev = ""

    while i >= 0:
        rev = rev + text[i]
        i = i - 1

    return rev


# palindrome check
def is_palindrome(text):
    text = text.lower()
    return text == reverse_text(text)


# remove vowels
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""

    for ch in text:
        if ch not in vowels:
            result = result + ch

    return result


# longest word
def longest_word(text):
    word = ""
    longest = ""

    for ch in text + " ":
        if ch != " ":
            word = word + ch
        else:
            if len(word) > len(longest):
                longest = word
            word = ""

    return longest


def word_frequency(text):
    text = text.lower()

    printed = ""
    word = ""

    print("Word Frequency:")

    for ch in text + " ":
        if ch != " ":
            word = word + ch
        else:
            if word != "":
                if word not in printed:

                    count = 0
                    temp = ""

                    for c in text + " ":
                        if c != " ":
                            temp = temp + c
                        else:
                            if temp == word:
                                count = count + 1
                            temp = ""

                    print(word + ":", count)
                    printed = printed + word + " "

            word = ""


# main analysis
def analyze_text(text):

    print("=== TEXT ANALYSIS ===")

    print("Words:", count_words(text))
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Reversed:", reverse_text(text))

    if is_palindrome(text):
        print("Palindrome: Yes")
    else:
        print("Palindrome: No")

    print("Without vowels:", remove_vowels(text))

    longest = longest_word(text)
    print("Longest word:", longest, "(" + str(len(longest)) + " letters)")

    word_frequency(text)


# main
text = input("Enter text: ")
analyze_text(text)