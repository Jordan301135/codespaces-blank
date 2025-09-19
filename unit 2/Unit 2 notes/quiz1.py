# Create a new document called quiz1.py copy/ paste the following questions
# on your document and answer the following questions.

# quiz rules:
# - There is no talking during the quiz
# - You may only use your classnotes and w3schools.com for reference
# - If you have a question about a quiz question, please raise your hand
# - Once finished, submit your code to your repository using the source control 
# button. Your commit should be "completed quiz 1."

# 1. Name and describe three (3) built-in functions in python. 
# Please write your responses in complete sentences.

# One built-in function in python is the print() function.
# The second built-in function in python is the input() function.
# The third built-in function in python is the String concatenation is where you can combine 2 or more strings
# together using the plus symbo

# 2. What data type will the following snippet of code output?
print(30/ 232)
# The data type that will be outputted is a float because the result is a decimal number.

# 3.  Identify and name the operator family each of the following
# symbols belongs to.

# and
# ==
# >

# the operator family for "and" is a logical operator.
# the operator family for "==" and ">" is a comparison operator.


# 4. Explain the difference between the = operator and the == operator.
# Please write your response in complete sentences.

# The difference between the operators is that the single equal sign (=) is an assignment operator, 
#The double equal sign (==) is a comparison operator.
#  The single equal sign is used to assign a value to a variable.
#eThe double equal sign is used to compare two values for equality.

# 5. Write code that takes a user’s input (as a string), 
# casts it to a float, and prints the result multiplied by 2.)

# user_input = input("Please enter a number: ")
# float_input = float(user_input)
# result = float_input * 2
# print(result)

# 6. What is the difference between a parameter and an argument?
# Please write your response in complete sentences.

# A parameter is a variable in the declaration of a function.
# An argument is the value that is sent to the function when it is called.

# 7. What is the difference between a function definition 
# and a function invocation? # Please write your response in 
# complete sentences.

# A function definition is where you define the function and its instructions.
# A function invocation is where you call the function to execute the instructions.

# 8. Why are functions useful in programming? Provide at least two reasons 
# and write your reasons in in complete sentences.

# Functions are useful in programming because they help to organize code into manageable sections.
# Functions also help to avoid code repetition by allowing you to reuse the same code multiple times.
# Functions also make code easier to read and maintain.

# 9. Write a code block that uses the appropriate operator for each scenario
# x = 5
x = 5
y = 20
# x is greater than y
print(x <y)
# x is greater than y
# x and 15 are both the same
print(x == 15)
# x and y are not the same
print(x != y)

# 10. Create a function that will take in two values. Your function should
# take in 1 value as a parameter, and the other value should be passed in by the
# user through the terminal. Your function should compare if the number passed in by
# the user is greater than the number passed in via the parameter and should print out
# the appropriat response of true or false.

def compare_numbers(param_num):
    user_num = float(input("Please enter a number: "))
    if user_num > param_num:
        print("True")
    else:
        print("False")