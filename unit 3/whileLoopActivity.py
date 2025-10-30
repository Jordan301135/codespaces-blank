# Activity 1
# Create a function that will print out a list of numbers based on
# what the user inputs. Your function should take in a user input,
# add the input to a list, and then print it out in the terminal.
# If the user enters the word "quit", the function loop
# should stop.

# create a function
# print out a list of numbers in terminal.
# take in a user input over and over again and add to list
# stop the loop when they type "quit"
from random import random


def numberLoop():
    numbers = []
    userNumber = input("Please type in a number: ")
    while userNumber.lower() != 'quit':
        numbers.append(userNumber)
        print(numbers)
        userNumber = input("Please type in a number: ")
    else:
        print("Loop has stopped.")

numberLoop()


# Activity 2
# Create a function that will continue to take in a number, 
# and when a user confirms they are done entering a number 
# add the numbers up and print out the result. Your function 
# should use a while loop where so long as the user does 
# not enter “quit”, it should continue adding numbers. 
# When they enter “quit” add the sum of numbers up.
  
# Hint: you will need to use the sum() function- check w3schools

def sumNumbers():
    numbers = []
    userNumber = input("Please type in a number to add to the sum: ")
    while userNumber.lower() != 'quit':
        numbers.append(int(userNumber))
        userNumber = input("Please type in a number to add to the sum: ")
    else:
        total = sum(numbers)
        print("The total sum of the numbers you entered is: " + str(total))
 
sumNumbers()


# Make a number guessing function. Your function should be able to
# take in a number as user input. Your functiom shpuld then evaluate
# if the user guessed the correct number. If the user enters that is above the
# correct number, it should output a message saying its to high and
# loop back to asking them to enter a number. If it's below the correct number
# it should output a message saying its too low and loop again. If they
# guess the correct number it should output a message saying they got it.

def numberGuessingGame():
    correctNumber = 77
    userGuess = int(input("Guess a number between 1 and 100: "))
    while userGuess != correctNumber:
        if userGuess < correctNumber:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
        userGuess = int(input("Guess a number between 1 and 100: "))
    else:
        print("Congratulations! You guessed the correct number.")

numberGuessingGame()