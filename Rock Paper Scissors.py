# import secrets to grab random value from the possible answer list
import secrets

print("Welcome to rock paper scissors!")
print("")

def rockPaperScissors():
	# ask for the user's input of either 'rock' 'paper' or 'scissors'
    user_input = input("In order to start the game, please input either, 'rock' 'paper' or 'scissors.'")
    print("")

    # create a list to hold the potential computer answers
    computerList = ['rock', 'paper', 'scissors']

    # if the user's input is one of the three correct values
    if user_input != 'rock' or 'paper' or 'scissors':
    	# make the computers answer one of the three values
        computerAnswer = secrets.choice(computerList)
    
    	# test for all possible outcomes of the game, print computer answer, print result and ask the user if they will play again or not
        if user_input == computerAnswer:
            print("The computer played", computerAnswer)
            endInput = input("It's a draw! Press 'Y' to play again or 'N' to stop the game.")
            print("")
        
        elif user_input == 'rock' and computerAnswer == 'paper':
            print("The computer played", computerAnswer)
            endInput = input("Paper beats rock, you lose! Press 'Y' to play again or 'N' to stop the game.")
            print("")
        
        elif user_input == 'rock' and computerAnswer == 'scissors':
            print("The computer played", computerAnswer)
            endInput = input("Rock beats scissors, you win! Press 'Y' to play again or 'N' to stop the game.")
            print("")
        
        elif user_input == 'paper' and computerAnswer == 'rock':
            print("The computer played", computerAnswer)
            endInput = input("Paper beats rock, you win! Press 'Y' to play again or 'N' to stop the game.")
            print("")
        
        elif user_input == 'paper' and computerAnswer == 'scissors':
            print("The computer played", computerAnswer)
            endInput = input("Scissors beat paper, you lose! Press 'Y' to play again or 'N' to stop the game.")
            print("")
            
        elif user_input == 'scissors' and computerAnswer == 'rock':
            print("The computer played", computerAnswer)
            endInput = input("Rock beats scissors, you lose! Press 'Y' to play again or 'N' to stop the game.")
            print("")
            
        elif user_input == 'scissors' and computerAnswer == 'paper':
            print("The computer played", computerAnswer)
            endInput = input("Scissors beat paper, you win! Press 'Y' to play again or 'N' to stop the game.")
            print("")
        
        # if the user says 'Y' restart the game, if they type 'N' have the game end
        if endInput == 'Y':
            print("")
            rockPaperScissors()
        elif endInput == 'N':
            print("Okay! Thanks for playing.")
   
# call the function to start the game 
rockPaperScissors()