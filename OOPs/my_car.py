# Write a Python class named Car with attributes like make, model, and year. Create an instance of the class and print its attributes.

class car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

my_car = car('BMW','SL200',2002)
print(f"car brand {my_car.make}")
print(f"car model {my_car.model}")
print(f"car year {my_car.year}")