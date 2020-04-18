from pickle import *

class Vehicle:
    def __init__(self):
        self.countOfWheels = None
        self.color = None
        self.make = None
        self.model = None
        self.numberOfseats = None
    
    def info(self):
        return "Car: %s %s %s %s %s" % (
            self.make,
            self.model,
            self.color,
            self.countOfWheels,
            self.numberOfseats
        )
        
myCars = []

mycar1 = Vehicle()
mycar1.countOfWheels = 4
mycar1.color = "Silver"
mycar1.make = "Toyota"
mycar1.model = "Corolla"
mycar1.numberOfseats = 4

mycar2 = Vehicle()
mycar2.countOfWheels = 4
mycar2.color = "Gray"
mycar2.make = "Honda"
mycar2.model = "Odyssey"
mycar2.numberOfseats = 8

# myCars.append(mycar1)
# myCars.append(mycar2)

myCars = [mycar1, mycar2]

carInfoFile = open('carInfo.txt', 'wb')
for car in myCars:
    print(car.info())
    dump(car, carInfoFile)
carInfoFile.close()

mycar3 = Vehicle()
f=open("carInfo.txt","rb")
mycar3=load(f)
print(mycar3.info())
