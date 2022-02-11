# Guess the number game

import random

print("Hello! Welcome to our game. The goal of the game is to guess the correct number, good luck!")
print("")

def randomNumberGuess():
    try:
        randomNumber = random.randint(1, 10)
        randomNumberString = str(randomNumber)
        userGuess = int(input("Guess a number between 1 and 10."))
        
        # if/else to check if the user's guess is equal to the random number
        if userGuess == randomNumber:
            print("")
            print("Congrats! You guessed the correct number!")
        else:
            print("")
            print("Sorry! You guessed the wrong number, better luck next time! The correct number was " + randomNumberString + ".")
            newGame = input("Do you want to play again? Type Y for 'yes' or N for 'no'")
            print("")
            
            if newGame == 'Y':
                randomNumberGuess()
            elif newGame == 'N':
                print("Okay! Thanks for playing.")
            
    except ValueError:
        print("")
        print("The input needs to be a number. Try again.")
        print("")
        randomNumberGuess()
        
randomNumberGuess()
