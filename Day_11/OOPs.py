from abc import ABC, abstractmethod


class Shape(ABC):

    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def discribe(self):
        print(f"It is {self.color} and {'flled' if self.is_filled else 'not filled'}")

    @abstractmethod
    def area(self):
        pass


class Square(Shape):

    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self._width = width

    def area(self):
        return self._width**2

    def discribe(self):
        super().discribe()
        print(f"area of square is {self.area():.1f}")


class Circle(Shape):

    def __init__(self, color, is_filled, redius):
        super().__init__(color, is_filled)
        self._radius = redius

    def area(self):
        return 3.24 * (self.__reduce__**2)

    def discribe(self):
        super().discribe()
        print(f"area of square is {self.area():.1f}")


class Triangle(Shape):

    def __init__(self, color, is_filled, hieght, base):
        super().__init__(color, is_filled)
        self._hieght = hieght
        self._base = base

    def area(self):
        return self._base * self._hieght / 2

    def discribe(self):
        super().discribe()
        print(f"area of square is {self.area():.2f}")


square = Square("red", True, 25)
square.discribe()
