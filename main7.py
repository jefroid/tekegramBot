class Figures:
    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def return_values(self):
        pass

    def calculate_perimeter(self):
        pass


class Circle(Figures):
    def __init__(self, radius: float):
        self._radius = radius

    def calculate_area(self):
        self._area = 3.14*self._radius**2

    def calculate_perimeter(self):
        self._perimetr = 2 * 3.14 * self._radius

    def return_values(self):
        return [self._radius, self._area, self._perimetr]


class Rectangle(Figures):
    def __init__(self, length: float, width):
        self._length = length
        self._width = width

    def calculate_area(self):
        self._area = self._width * self._length

    def calculate_perimeter(self):
        self._perimetr = self._width*2 + self._length*2

    def return_values(self):
        return [self._width, self._length, self._area, self._perimetr]


class Square(Rectangle):
    def __init__(self, side: float):
        self._side = side

    def calculate_area(self):
        self._area = self._side**2

    def calculate_perimeter(self):
        self._perimetr = self._side*4

    def return_values(self):
        return [self._side, self._area, self._perimetr]


def main():
    circle = Circle(10)
    square = Square(5)
    rectangle = Rectangle(5, 10)
    circle.calculate_area()
    square.calculate_area()
    rectangle.calculate_area()
    circle.calculate_perimeter()
    square.calculate_perimeter()
    rectangle.calculate_perimeter()
    print(circle.return_values())
    print(square.return_values())
    print(rectangle.return_values())


main()
