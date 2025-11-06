# For Loops - A type of contruct that runs code instructions
# a finite amount of times over a group of data.

halloweenBag=['Snickers', 'Hershey Bar', 'Fruit Chews', 'Skittles', 'M&Ms']

# i is a variable and is short for iterator.
for candy in halloweenBag:
    print(candy)
    print(' I have ' + candy + ' in my bag!')

# 0 is false
# 1 is true





for x in range(3):
    print('true or false: 3 is greater than 2')
    answer=input()
    if answer != 'true':
        print('wrong, try again')
        print('attempt' + str(x))
    else:
        print('great!')
        break


# Use a for loop to ask a user to type in 5 words and print each word out in
# the terminal. Once the user has finshed typying 5 words.
# the for loop should end.

# Clarification: Program should ask the user to type in one word. Then the pprogram
# should print it out and ask them to type in another word. Your progra
# should do this 5 times.

# Hint # 1: you should use the range() funtion.

for x in range(5):
    word=input("Please type in a word: ")
    print(word)

# looping through strings:
word = "Python"
for letter in word:
    print(letter)


ShoppingPrices = [3.00, 5.40, 7.20, 9.00, 10.40, 11.00]
total = 0

for item in ShoppingPrices:
    total += item
    print(total)

print(total)


student = ['jordan', 'joel', 'devonte', '...']

present = []
absent = []

scannedIn = True
for student in studentBody:
    print('Is ' + student + 'scanned in today?')
    response = input()

    # if student =! scannedIn
    # move to absent list
    # absent.append(student)
    # else put them in present list
    # present.append(student)