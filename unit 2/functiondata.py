# Howto create a fuction that passes data

# Step 1. create a function definition
#def bnbRefung(username, refundAmount):
    #print('soryy ' + username + 'for you cancellation')
    #print('We wll refund $' + str(refundAmount)+ 'amout yto your bank')

# Step 2. Call the function/ execute instructions
#bnbRefung( 'Mary',5)

#def brithdy(name, date):
    #print('My name is' + name + date)

#brithdy(' Jordan Wells ',' and my birthday is December 27. ')

#def dollarConvert(dollar):
    #penneis = dollar * 100
   #print ('My' + str(dollar) + ' dollar(s) is equal to' + str(pennies) + 'pennies')
#dollarConvert(13)

def triangleArea(width, length):
    area = 0.5 * width * length
    print ('The area of a triangle with the width of ' + str(width) + ' and length of ' + str(length) + ' is ' + str(area))

triangleArea(15, 20)

def rectangleArea(width, length, height):
    area = width * length * height
    print ('The area of a rectangle with the width of ' + str(width) + ', length of ' + str(length) + ', and height of ' + str(height) + ' is ' + str(area))

rectangleArea(20, 15, 23)

def temperatureConvert(fahrenheit):
    celsius = (fahrenheit * 5/9) - 32
    print (str(celsius) +  ' degrees celsius is equal to.' + str(fahrenheit) + ' degrees fahrenheit.')
temperatureConvert(100)