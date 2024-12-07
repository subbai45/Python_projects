# Create a Laptop class with private attributes for brand and price. Use getter and setter methods to access and modify these attributes.

class laptop:
    def __init__(self,brand,price):
        self.__brand = brand
        self.__price = price
    def get_brand(self):
        return self.__brand
    def get_price(self):
        return self.__price
    def set_brand(self,brand):
        self.__brand=brand
    def set_price(self,price):
        self.__price=price
# Main Program
lap = laptop('Hp',2000)
print("Laptop brand: ",lap.get_brand())
print("Laptop price: ",lap.get_price())

lap.set_brand('Mac')
lap.set_price(12000)

print("Laptop brand: ",lap.get_brand())
print("Laptop price: ",lap.get_price())