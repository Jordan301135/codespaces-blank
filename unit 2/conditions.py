# Conditional Statements - code introductions that
# have different outcome based on the inputted data.
#Input condition and output

#Conditional Statement Syntax
#if keyword - Controls the condition we want to satisfy

# else keyword - Our defult outcome. The thing that
# happens when our condition are NOT satisfied

weather = input(' what is the weather like today? ')
if weather == 'sunny':
    print(" It's is beautiful outside. Bring sunglasses")
else:
   print(" I can't tell you the weather, but have a good day")
if weather == 'rainy':
    print(" remember to bring an umbrella and a rain coat")
else:
    print(" I can't tell you the weather, but have a good day")
if weather == 'snowy':
    print(" remember to wear a warm coat and boots")
if weather == 'chilly':
   print(" remember to bring a jacket")
else:
    print(" I can't tell you the weather, but have a good day")


from turtle import down


password = input("Please enter your password: ")
if password == 'Kobe824':
    print(" welcome back Kobe Bryant")
else:
    print(" incorrect password, please try again") 


vanilla = 0 # number of ice cream bars in stock
chocolate = 10
strawberry = 10

def iceCreamShop(flavor):
    if flavor == "vanilla":
        print("we have vanilla in stock")
    elif flavor == "chocolate":
        print("we have chocolate in stock")
    elif flavor == "strawberry":
        print("we have strawberry in stock")
    else:
        print("we don't have that ice cream")

iceCreamShop("chocolate")

down = input("What down is it? ")
yards = int(input(" How many yards do you need to get another first down? "))

if down == 1 and yards <= 5:
    print(" You should run the ball")
elif down == 2 and yards <= 5:
    print(" You should pass the ball")
elif down == 3 and yards <= 5:
    print(" You should kick a field goal")
else:
    print(" You should punt the ball ")


def Permit(age):
    if age >= 16:
        print(" You can get a permit")
    else:
        print(" You cannot get a permit ")
Permit(16)



def testTakerPermit(age):
    if age >= 16:
        print(" You may take the permit test. ")
    else:
        print(" You are not old enough ")

testTakerPermit(18)


def numberCheck(number):
    if number > 0:
        print(" The number is positive ")
    elif number < 0:
        print(" The number is negative ")
    else:
        print (" The number is zero ")

numberCheck(-12)


def gradeScore(score):
    if score >= 90:
        print(" You got an A")
    elif score >= 80:
        print(" You got a B")
    elif score >= 70:
        print(" You got a C")
    else:
        print( " You got a F")

gradeScore(91)