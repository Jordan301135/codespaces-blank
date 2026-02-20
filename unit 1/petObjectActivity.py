# Create a pet animal class function. The class should have 4 properties
# and 4 methods.

# Then create 3 pets object. Each pet should have unique
# properties and use at least 1 method.


class Pets_Contructor:
    def __init__(self, name, type, age, color):
        self.dogs = name
        self.fish = type
        self.snake = age
        self.mouse = color
        
    def wildness(self,food):
        if food == 0:
            print(self.name + 'has a attitude and made a mess in the kitchen')
        else:
            print(self.name + 'is calm because they ate')

    def sleep(self):
        print(self.name + 'is tired')

    def bathroom(self):
        print(self.name + 'needs to got to the bathroom')


pet_1 = Pets_Contructor('Brandon', 'dog', 4, 'black')
pet_2 = Pets_Contructor('Slime', 'Snake', 6, 'white')
pet_3 = Pets_Contructor('Mittenz','Cat', 7, 'Black and Grey')

pet_1.wildness(0)
