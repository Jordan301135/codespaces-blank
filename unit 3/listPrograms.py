# Print the of 4 foods and do the following:
# - Print the first and last item based on the list index position
# - Replace the second list item with a new food item and then print the list
# - Bonus: slice the list with the middle two items and then print the result.
def FoodList():
    foodList = ['pizza', 'cheeseburger', 'spaghetti', 'fruit salad']
    print(foodList[0])
    print(foodList[2])
    print(foodList[3])
    foodList[1] = 'cheesesteak'
    print(foodList)
    print(foodList[1:3])

FoodList()


# If user enters "morning", inform the user that it is breakfast time and show a list of 3 breakfast meals.
# If user enters "afternoon", inform the user that it is lunch time and show a list of 3 lunch meals.
# If user enters "evening", inform the user that it is dinner time and show a list of 3 dinner meals.
# If user enters anything else, inform the user that the entry is invalid.

def mealtimeList():
    time = input('please enter the time of day (morning, afternoon, evening): ')
    if time == 'morning':
        print('it is breakfast time')
        breakfast = ['pancakes', 'waffles', 'french toast']
        print(breakfast)
    elif time == 'afternoon':
        print('it is lunch time')
        lunch = ['sandwich', 'salad', 'mozarella sticks']
        print(lunch)
    elif time == 'evening':
        print('it is dinner time')
        dinner = ['lasagna', 'salmon', 'chicken alfredo']
        print(dinner)
    else:
        print('invalid entry, please try again')

mealtimeList()