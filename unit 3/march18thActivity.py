# In your unit 3 folder, create a new document called activityMar19.py Copy and paste the questions into your document and then
#  answer the following questions. You are permitted to use your notes, w3schools, and work together to answer the questions.
# do your best to complete all questions. This activity is due at the end of class.


# 1. In your own words, what is the difference between a python class and a python object?
# Please write your resonse as a string data type. 
"A Python class is like a blueprint or template that defines what data (properties) and behaviors (methods) an object will have."
"A Python object is a specific thing created from that class, with its own actual data stored in memory based on the blueprint."
# 2. In your own words, what is a object property and and object method? Please
# write your response as a string data type.

"An object property is a variable that belongs to an object and stores information about it (like a car’s color or speed). "
"An object method is a function that belongs to an object and uses that objects data to do something, like changing its state or "
"returning information."

# 3. Create a unique python class. Your class should have 5 properties and 3 mtethods. 
# each method should do one of the following; 
# 1 method must do some type of operation with data; an arithmetic, logical, or comparison operation
# 1 method must take in a parameter and do some operation on the parameter
# 1 method must do some type of conditional (if/else) logic. 

class GameCharacter:
    def __init__(self, name, health, attack_power, defense, level):
        self.name = name           # string
        self.health = health       # int
        self.attack_power = attack_power  # int
        self.defense = defense     # int
        self.level = level         # int

    # 1) Method that does an arithmetic operation with data
    def attack(self, enemy_defense):
        # damage is attack_power minus enemy_defense, but not less than 0
        damage = self.attack_power - enemy_defense
        if damage < 0:
            damage = 0
        return damage

    # 2) Method that takes in a parameter and does an operation on that parameter
    def heal(self, amount):
        # increase health by the given amount
        self.health += amount
        return self.health

    # 3) Method that does conditional (if/else) logic
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False


# Example of using the class
hero = GameCharacter("Archer", 100, 25, 10, 1)

print(hero.is_alive())          # True
print(hero.attack(5))           # Uses arithmetic and comparison
print(hero.heal(20))            # Uses parameter and arithmetic
print(hero.is_alive())          # Conditional check