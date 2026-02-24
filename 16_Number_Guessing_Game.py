# Q16: Number Guessing Game

import random

best_score = 0   # store minimum attempts used

play = "yes"

while play == "yes":
    
    # number guessing game with difficulty levels
    print("Choose Difficulty:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-1000)")

    level = input("Enter choice: ")

    if level == "1":
        secret = random.randint(1, 50)
        max_range = 50
    elif level == "2":
        secret = random.randint(1, 100)
        max_range = 100
    elif level == "3":
        secret = random.randint(1, 1000)
        max_range = 1000
    else:
        print("Invalid choice. Defaulting to Medium.")
        secret = random.randint(1, 100)
        max_range = 100
    
    attempts_left = 7
    attempts_used = 0
    guessed_correct = False

    print("\nI have chosen a number between 1 and", max_range)
    print("You have 7 attempts.")

    while attempts_left > 0 and guessed_correct == False:

        try:
            guess = int(input("Enter your guess: "))
            attempts_used = attempts_used + 1

            if guess == secret:
                print("Congratulations! You guessed correctly.")
                print("Attempts used:", attempts_used)
                guessed_correct = True

                # best score tracking
                if best_score == 0:
                    best_score = attempts_used
                else:
                    if attempts_used < best_score:
                        best_score = attempts_used

            else:
                attempts_left = attempts_left - 1

                if guess > secret:
                    print("Too high!")
                else:
                    print("Too low!")

                # hint within 5
                difference = guess - secret
                if difference < 0:
                    difference = difference * -1

                if difference <= 5:
                    print("Hint: You are very close!")

                print("Attempts remaining:", attempts_left)

        except:
            print("Enter a valid number!")

    if guessed_correct == False:
        print("You lost. The number was:", secret)

    if best_score != 0:
        print("Best score so far:", best_score)

    play = input("Play again? (yes/no): ")