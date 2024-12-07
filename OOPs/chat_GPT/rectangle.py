# Rectangle Class:
#
# Write a Rectangle class with attributes for length and width.
# Add methods to calculate the area and perimeter of the rectangle.(A = L * W)
# Create an object of Rectangle, set the dimensions, and display the area and perimeter.(P = 2(L + W))

# Finding the length of the rectangle
def length():
    while True:
        try:
            leng = float(input("Enter the length of the rectangle: "))
            return leng
            break
        except ValueError:
            print("\tEnter only Digits")
# Finding the width of the rectangle
def width():
    while True:
        try:
            width = float(input("Enter the width of the rectangle: "))
            return width
            break
        except ValueError:
            print("\tEnter only Digits")

# Creating the class of rectangle
class rectangle:
    def measurements(self):
        self.leng = length()
        self.width = width()

    def area_and_peri(self):
        self.area = self.leng * self.width
        self.perimeter = 2 * (self.leng + self.width)
    def display_measurements(self):
        print(f"Length of rectangle is {self.__dict__}")
        print("=" * 50)
        print("\tArea and perimeter of RECTANGLE")
        print("=" * 50)
        for key,val in self.__dict__.items():
            print(f"\t\t\t{key}--->{val}")
        print("=" * 50)

# Main Program
#Creating the object of the class rectangle
rec = rectangle()
rec.measurements() # creating the instance method to find the length and width
rec.area_and_peri() # creating the instance method to calculate the area and perimeter of the rectangle
rec.display_measurements() # creating the instance method to display the calculated part

