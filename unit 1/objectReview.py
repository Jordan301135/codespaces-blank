# 1. In your own words, decribe what a class property is. Please write
# you response in string.
"a class is a bulit-in function for creating objects."


# 2. In your own words, decribe what a class method is. Please write
# you response in string.
"Methods define the behavior of objects"

# 3. Create a student class function. This function should create unique student
# objects. Your class nees to have 4 properties and 3 methods.
# Once you created you class, create 2 student objects. Each should be using a method from your class.

class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print("ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grade:", self.grade)

    def update_grade(self, new_grade):
        self.grade = new_grade
        print(self.name + "'s grade has been updated to", self.grade)

    def is_passing(self):
        if self.grade >= 60:
            print(self.name + " is passing.")
        else:
            print(self.name + " is failing.")


student1 = Student(1, "Alice", 20, 75)
student2 = Student(2, "Kobe", 22, 55)

student1.display_info()
student1.is_passing()

student2.display_info()
student2.update_grade(35)
student2.is_passing()

# 4. Create a video game character class function. This function
# should create basic video game character object.
# The character can be inspired by fanatasy games or sports games.
# Your class nees to have 4 properties and 3 methods.
# Once you created you class, create 2 characters objects. 
# Each should be using a method from your class.

class DragonBallCharacter:
    def __init__(self, name, power_level, health, form):
        self.name = name
        self.power_level = power_level
        self.health = health
        self.form = form

    def attack(self):
        print(self.name + " attacks with a power level of " + str(self.power_level) + "!")

    def transform(self, new_form, power_boost):
        self.form = new_form
        self.power_level += power_boost
        print(self.name + " transforms into " + self.form + "!")

    def show_stats(self):
        print("Name:", self.name)
        print("Power Level:", self.power_level)
        print("Health:", self.health)
        print("Form:", self.form)


character1 = DragonBallCharacter("Gogeta", 20000, 100, "Ultra")
character2 = DragonBallCharacter("Vegito", 21000, 100, "Ultra")

character1.show_stats()
character1.attack()

character2.show_stats()
character2.attack()