# 1. Create a function that checks the price of an item. and depending 
# on the item they will get a specific discount amout. Your function
# should take in the item price as an input from the user. If the user's 
# item cost between 50 and 75 dollars, they will recieve a 15% discount.
# If the item is above 75 dollars, they will recieve a 25%% discount.
# Your program should put out and inform the user how much of a 
# discount they will get and what the new total for the item be with
# the applied discount.

# Take a price and depending on the price amount the user will get 
# a 15%, 25% discount or no discount.

# input - we need to take in the item price as an input
# the output needs to calculate and show the discount amount
# needs to be a function
# if price is > 50 but < 75 = should get 15% off
# if price is > 75 = should be 25% off
# conditional statement if/ else

def discount():
    price = int(input("How much is the item?"))
    if price > 50 and price < 75:
        sum = price * .15
        total = price - sum
        print(sum)
        print("your new total is" + str(total))

    elif price > 75:
        sum = price*.25
        total = price - sum
        print(sum)
        print("your new total is" + str(total))

    else:
        print("sorry no discount")

discount()