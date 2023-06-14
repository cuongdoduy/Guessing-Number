"""
Project 1 - Number Guessing Game
--------------------------------

NOTE: If you prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random
from statistics import median
from statistics import mode
from statistics import mean

def start_game(best_score):
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Save their attempt number to a list.
    6. At the end of the game, show the player, 1) their number of attempts, 2) the mean, median, and mode of the saved attempts list.
    7. Ask the player if they want to play again.
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    print("Welcome to the Number Guessing Game!")
    print("************************************")
    print(f"The current best score is: {best_score}")
    print("Try to guess the number between 1 and 100")
    print("************************************")
    random_number = random.randint(1, 100)
    attempts = []
    while True:
        try:
            guess = int(input("Pick a number between 1 and 100: "))
            if guess < 1 or guess > 100:
                raise ValueError("The number is outside the range.")
            else:
                attempts.append(guess)
                if guess == random_number:
                    print(f"You got it! The number was {random_number}")
                    break
                elif guess > random_number:
                    print("It's lower")
                else: 
                    print("It's higher")
        except ValueError as err:
            print("{}".format(err))
            continue
    print(f"It took you {len(attempts)} attempts to guess the number.")
    print(f"The mean of your attempts is: {mean(attempts)}")
    print(f"The median of your attempts is: {median(attempts)}")
    print(f"The mode of your attempts is: {mode(attempts)}")
    best_score = min(len(attempts), best_score)
    play_again = input("Would you like to play again? (Y/N) ")
    if play_again.lower() == "y":
        start_game(best_score)
    else:
        print("Thanks for playing! Goodbye!")
        exit()


# Kick off the program by calling the start_game function.
best_score = 100
start_game(best_score)