# A python dictionary is a collection type that stores values that describe 
# unique data
# IT IS AN OBJECT
# Its similar to a class object but with less rules
# There are no methods on dictionaries

SrProm = {
"name": "senior prom",
"date": "May 8th 2026",
"gradeLevel": "12th"
}

srFieldTrip = {
"name": "senior Field Trip ",
"date": "May 22nd 2026",
"gradeLevel": "12th",
"timeLeaving": "6 AM",
"timeReturning": "12AM"
}

graduation = {
"name": "senior graduation ",
"date": "June 2nd 2026",
"gradeLevel": "12th",
}

print(graduation["date"])

# class is function that CREATES OBJECTS - these objects need to follow the class
# rules
# dictionaries are natural objects
class event():
    def __init__(self, name, date, gradeLevel):
        self.name = name
        self.date = date
        self.gradeLevel = gradeLevel

events = [graduation, srFieldTrip, SrProm]
#print(events)

for special_Occassion in events:
    print(special_Occassion["name"] + " - " + special_Occassion["date"])