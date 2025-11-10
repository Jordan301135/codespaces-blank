# create a new document called pythonReview.py and answer the following
# questions. 

# Question 1
# Build a program that determines if a student has submitted their class work 
# and homework assignment. The program should use an operator that allows 
# for evaluating 2 conditions and determining if the conditions are true 
# or false.

def review_submissions():
    class_work_submitted = input(" Has the class work been submitted? (true or false): ").lower() == 'true'
    homework_submitted = input(" Has the homework been submitted? (true or false): ").lower() == 'true'

    if class_work_submitted and homework_submitted:
        print("Both assignments have been submitted.")
    else:
        print("One or both assignments are missing.")

# hint: find the a operator that allows you to evaluate 2 condtions.

# Question 2
# Create a function that will take in a string as an argument and output 
# that string in reverse order.

def reverse_string(input_string):
    print (input_string[::-1])

reverse_string('hello')

# hint: look into string reverse in w3schools

# Question 3
# Create a number guessing function where the program will continuously 
# ask the user to enter a number until the guess the number correctly. 
# Your program should also give the user information on if their guess 
# is close to the correct number. If the guess is above the correct number 
# it should tell the user it is too high and try again. 
# If the guess is below the number, it should tell the user it is too low, 
# it should tell them it is too low and to guess again. Once the user gets 
# it correct the program should congratulate them, stop, and tell them how 
# many attempts they made.

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