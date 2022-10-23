import math
import statistics as stat
from datetime import datetime


class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return "Area: {}\nRooms: {}\nPrice: {}\nAddress: {}".format(
            self.area, self.rooms, self.price, self.address
        )


class House(Property):
    def __init__(self, area, rooms: int, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return super().__str__() + "\nPlot: {}".format(self.plot)


class Flat(Property):
    def __init__(self, area, rooms: int, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return super().__str__() + "\nFloor: {}".format(self.floor)


house1 = House("Silesia", 2, 100, "Chryzantem 10 Ruda Śl", 160)
print(str(house1))

flat1 = Flat("Silesia", 2, 100, "Chryzantem 10 Ruda Śl", 2)
print(str(flat1))
