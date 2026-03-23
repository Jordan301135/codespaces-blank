# Libaray = place that stories alot of books/ infomation.

# Python Libraries = files/folders that contain functions and data that we can
# use quickly and easily. These are code intructions that wewre already written
# for us. We just need to call it.

# We use the IMPORT key word to bring in libraries/ modules into our code.

import example




newStudent = example.Student(12947503, 'James', 28, 90)
print(newStudent.name)

newStudent.display_info()
newStudent.update_grade(100)
newStudent.is_passing()



import example

newDragonBallCharacter = example.DragonBallCharacter('Broly', 40000000000000, 320000000000000, 'Legendary Super Sayian 3')

newDragonBallCharacter.show_stats()
newDragonBallCharacter.attack()