class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, origin, weight, height):
        self.origin = origin
        self.weight = weight
        self.hight = height

    def getArea(self):
        return self.width * self.height

    def printCoordinates(self):
        top_right = self.starting_point.coordX + self.weight
        bottom_left = self.starting_point.coordY + self.height
        print('Origin (X)): ' + str(self.origin.x))
        print('Origin (Y)): ' + str(self.origin.y))
        print('End Point X-Axis (Top Right): ' + str(top_right))
        print('End Point Y-Axis (Bottom Left): ' + str(bottom_left))


def build_rectangle():
    rectangle_origin = Point(50, 100)
    rectangle = Rectangle(main_point, 90, 10)

    return rectangle


rectangle = build_rectangle()

print(rectangle.getArea())
rectangle.printCoordinates()
