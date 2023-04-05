class Vehicle():
    def __init__(self):
	    self.cls = input("Enter the vehicle type: ") 

class Automobile(Vehicle):
    def __init__(self, cls):
        self.cls = cls
        self.year = input("Enter the year: ")
        self.make = input("Enter the make: ") 
        self.model = input("Enter the model: ") 
        self.doors = input("Enter the amount of doors: ") 
        self.roof = input("Enter sunroof or solid: ")

    def Print(self):
        print("Vehicle type: ", self.cls)
        print("Year: ", self.year)
        print("Make", self.make)
        print("Model: ", self.model)
        print("Number of doors: ", self.doors)
        print("Type of roof: ", self.roof)
        
car1 = Vehicle()
Automobile(car1.cls).Print()

