# program to calculate area of circle by using OOPs concept
import math
import sys
class circle():
    def readvalues(self):
        self.rad = float(input("Enter the radius of the circle: "))
        print(id(self))
    def area_circle(self):
        self.area = math.pi * self.rad * self.rad
        print(id(self))
    def display_res(self):
        print(f"Area of circle for radius {self.rad} is {round(self.area,2)}")
        print(id(self))
# main program
c=circle()
c.readvalues()
c.area_circle()
c.display_res()
print(sys.getsizeof(c))
