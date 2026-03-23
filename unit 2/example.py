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
        if self.grade >= 59:
            print(self.name + " is passing.")
        else:
            print(self.name + " is failing.")


student1 = Student(1795395, "Ashley", 20, 75)
student2 = Student(10824, "Kobe", 22, 55)

student1.display_info()
student1.update_grade(62)
student1.is_passing()

student2.display_info()
student2.update_grade(84)
student2.is_passing()



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

character1 = DragonBallCharacter("Gogeta", 18000000000000000000000000000000000000000000000000, 180000000000000000000000000000000000000000000000, "CC Gogeta")
character2 = DragonBallCharacter("Vegito", 21000000000000000000000000000000000000000000000000, 300000000000000000000000000000000000000000000000, "CC Vegito")

character1.show_stats()
character1.attack()

character2.show_stats()
character2.attack()