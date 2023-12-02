
"""
Lab 1 Solution Code
"""
# import the necessary libraries.
from random import randint

# have the computer generate a random number.
number = randint(0, 100)

# ask the user to guess.
# the lowest possible number guesses can be is 1.
guess = int(input("Enter a guess: "))
guesses = 1

# we have our while loop make the user
# keep guessing as long as they haven't guessed
# correctly. 
while guess != number:
  guesses += 1
  if guess < number:
    print("Too low!")
  elif guess > number:
    print("Too high!")
  # we have them guess again, so that the
  # conditional in the while loop has an 
  # updated guess to work with.
  guess = int(input("Enter a guess: "))

# this line will only run if the user guesses correctly.
# guess must be equal to number now.
print("Congratulations! You got it!")

print("It took you", guesses, "tries.")


"""
Lab 1 Extension Solution Code
"""

# import the necessary libraries.
from random import randint

print("Welcome to the guessing game!")

# set persistent variables OUTSIDE of the while loop.
high_score = -1
high_score_haver = ""
playAgain = "y"

# this is the while loop that contains the game.
while playAgain == "y":
  # now, we are in the game.
  # have the computer choose the random number. 
  number = randint(2, 5)
  guesses = 1

  guess = int(input("Enter a guess: "))
  
  while guess != number:
    guesses += 1
    if guess < number:
      print("Too low!")
    elif guess > number:
      print("Too high!")
    guess = int(input("Enter a guess: "))
    
  print("Congratulations! You got it!")
  
  print("It took you", guesses, "tries.")

  # check if the high score is unset or has been beat.
  if guesses < high_score or high_score == -1:
    print("You set a new high score!")
    # update the high score
    high_score = guesses
    # update the high score name
    high_score_haver = input("Type your name: ")
  else:
    print("The current high score is", high_score,
          "and was set by", high_score_haver, ".")
  
  playAgain = input("Type y and press enter to play again.")
