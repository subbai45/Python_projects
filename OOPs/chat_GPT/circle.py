# Circle Class:
#
# Create a class Circle that has an attribute for the radius.
# Add methods to calculate the area and the circumference of the circle.
# Create a Circle object, set the radius, and display the area and circumference.
import math
def radius_check():
    while True:
        try:
            rad = float(input("Enter the radius of the circle: "))
            return rad
            break
        except (ValueError,NameError):
            print("\tEnter only digits")
class circle:
    def __init__(self):
        self.PI = math.pi
    def radius(self):
        self.rad = radius_check()
    def area_circumference(self):
        self.area = self.PI * self.rad # A = PI * RADIUS
        self.circum = 2 * (self.PI * self.rad)
    def display(self):
        print("=" * 50)
        print("\tCIRCLE DETAILS")
        print("=" * 50)
        for key,val in self.__dict__.items():
            print(f"\t\t{key} :- {round(val,2)}")
        print("=" * 50)

# Main program
c = circle()
c.radius()
c.area_circumference()
c.display()