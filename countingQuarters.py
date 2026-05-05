# Create a function that will determine how many quarters coins a user will get in exchange for their dollar amount. 
# - The dollar amount should be passed in as a parameter. 
# - The function should calculate how many quarters they will get back (ex. 1 dollar = 4 quarters)
# - The function should print out a message telling the user how much money they inserted and how many quarters they are getting back. 

def dollar_to_quarters(dollar_amount):
    quarters = int(dollar_amount * 4)  # 4 quarters per dollar
    print("You inserted $" + str(round(dollar_amount, 2)))
    print("Total: " + str(quarters) + " quarters")

                            # Usage

dollar_to_quarters(8)