# Python OOP - Object Oreinted Programming

# Object - A representation
# of some complex data structure.
# *data = data types(... and functions in this case)
# Although they maybe the same thing, objectively, objects
# can different characteristics/ features

# Class - is a constuctor / blueprint for creating
# objects

class computers:
    def __init__(self, name, color, shape, storage, portability, camera, ram, processor):
        self.name = name
        self.color = color
        self.shape = shape
        self.storage = storage
        self.portability = portability
        self.camera= camera
        self.ram = ram
        self.processor = processor

apple_1 = computers("mac m4", "black", 10.00, 320, True, True, "60", 'm4')
apple_2 = computers("apple m4", "white", 10.00, 320, True, True, 80, 'm4')

      # def bluetoothConnection(self):
      #       print("")

      # def internetConnectivity(self):
      #       print("")

      # def powerOn(self):
      #    print("")




# class Phones:
#    def __init__(self, storage, carrier, size, color, camera, name, warrenty, price, brand):
#       self.storage = storage
#       self.carrier = carrier
#       self.size = size
#       self.color = color
#       self.camera = camera
#       self.name = name
#       self.warrenty = warrenty
#       self.price = price
#       self.brand = brand

# phone1 = Phones(16,'att',13.00,'yellow',False, 'brickPro' False, 300.00, 'brick')
# phone2 = Phones(32,'att',7.00,'yellow',False, 'brick' False, 100.00, 'brick')
class NBA2KMyCareer:
   def __init__(self, Finshing, Shooting, Playmaking, Defense, Rebounding):
        self.Finishing = Finshing
        self.Shooting = Shooting
        self.Playmaking = Playmaking
        self.Defense = Defense
        self.Reboundindg = Rebounding