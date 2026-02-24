# Q1: Personal Bio Card

# taking user details to display inside a card
name = input("Enter your name: ")
age = input("Enter your age: ")
course = input("Enter your course: ")
college = input("Enter your college: ")
email = input("Enter your email: ")

# fixed width for value section
width = 31

print("=" * 46)
print("||" + " " * 13 + "STUDENT BIO CARD" + " " * 13 + "||")
print("=" * 46)

print("|| Name    : " + name + " " * (width - len(name)) + "||")

age_text = age + " years"
print("|| Age     : " + age_text + " " * (width - len(age_text)) + "||")
print("|| Course  : " + course + " " * (width - len(course)) + "||")
print("|| College : " + college + " " * (width - len(college)) + "||")
print("|| Email   : " + email + " " * (width - len(email)) + "||")

print("=" * 46)