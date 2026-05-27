#guessing_game.py is a number guesssing game that guesses number between 1 and 100

import random
secret_number = random.randint(1,100)
attempts = 0
max_attempts = 7

print("Welcome to the Number Guessing Game!")

print("Guess a number between 1 and 100.")

print("You have 7 attempts.\n")

while attempts < max_attempts:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess == secret_number:
            print(
                f"\nCorrect! "
                f"You guessed the number in {attempts} attempts."
            )

            break

        elif guess > secret_number:

            print("Too high!\n")
        
        else:

            print("Too low!\n")

            
        remaining = max_attempts - attempts

        print(f"Remaining attempts: {remaining}\n")

        
    except ValueError:

        print("Invalid input! Please enter a number.\n")

else:

    print(
        f"\nGame Over! "
        f"The correct number was {secret_number}."
    )