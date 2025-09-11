# Fuctions- is a set of intructions labeld under
# a custom name that the computer will rum.

# Function Snytax (rules of how its written)
# functions have 2 phases: function definition and
#function call

#fuction definition
# we are describing the instruction for our custom code.
# we are adding help logic to the computers vocabulary.
# this code does not run- it only gives the computer the meaning
#not the action

def example():
    print('good morning') # 1 instruci=tion print good morning

# PHASE 2: fucion call
# once we have the definition, we can now run the intructions
# by writiting the function name.

# we indent to inform the computer that we are about nto write
# code intructions. If we don't we will nget an error.
def example():
    print('good day')
    a = input ('enter a number:')
    print(a)

def math():
    a = input("please enter a number")
    b = 30
    print("here is your result!")
    print(int(a)+b)

math

# create a function that will calculate 2 numbers
# with different arithmetic operators
def calculate():
    numx = input('please enter a number:')
    numy = input('please enter another number')
    print(numx, numy)

calculate()