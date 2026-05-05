class Smartphone():
    def __init__(self, brand, model, battery_level):
        self.brand = brand
        self.model = model
        self.battery_level = battery_level

    def charge(self):
        print("current battery level"+ str(self.battery_level))
        charge = input("Would you like to charge? Enter y to charge and n to NOT charge")
        if charge == 'y':
            while self.battery_level < 100:
                self.battery_level += 10
                print("new battery level = " + str(self.battery_level))
                charge = input("Would you like to continue charging")
        elif charge == 'n':
            print("battery level = " + str(self.battery_level))

        
        else:
            print("current battery level = " + str(self.battery_level))

    def get_status(self):
        print(" Here is your phone info: " + " phone brand = " + self.brand + " phone model = " + self.model)

Mom = Smartphone("Apple Iphone", "Iphone 17 Pro Max", 20)
Dad = Smartphone("Google", "Google Pixel 10 Pro Fold", 60)
Sister = Smartphone("Samsung", "Android Galaxy S26", 0)
Brother = Smartphone("PlusOne", "PlusOne 15", 50)


Mom.get_status()
Dad.get_status()
Sister.get_status()
Brother.get_status()


Mom.charge()
Dad.charge()
Sister.charge()
Brother.charge()