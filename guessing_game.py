# Number Guessing Game
#
# March 15 2020 by Rob Smith
#
# Allow the user to guess a number between 1 and 10
# App allows user to keep guessing until they get the correct number
# When user gets the correct number it confirms the correct number and shows how
# many attempts it took them to guess the number

import random
# secret_number = random.randint(1,10)

# Function to confirm the guess is a number between 1 and 10
# If not a number or blank it advises the guess is not valid
# and asks for another input
def get_guess():
    while True:
            try:
                guess = int(input('Guess a number between 1 and 10: '))
                if guess not in range(1,11):
                    get_guess()
                else:
                    return guess
            except:
                print("That's not a valid option!")

# Takes the valid guess from get_guess fuction and tests if it mateces the
# secret number - if it does game is finished
# If the user guess does not match it advised if the secret number is
# higher or allow and allows the user to guess again
# After guessing the secret number it gives the user an option to 
# play again
def check_guess(guess):
    secret_number = random.randint(1,10)
    total_guesses = 0
    while secret_number != "guess":
        total_guesses += 1
        if guess > secret_number:
            print("Your guess was too high sorry. Try Again")
            guess = get_guess()
        elif guess < secret_number:
            print("Your guess was too low sorry. Try Again")
            guess = get_guess()
        else:
            print(f"Well done you guessed the secret number which was {secret_number} in only {total_guesses} attempts")
            playagain = str(input('Would you like to play again? (Y or N) '))
            if playagain == "Y" or playagain == "y":
                total_guesses = 0
                check_guess(get_guess())
            break

check_guess(get_guess())


