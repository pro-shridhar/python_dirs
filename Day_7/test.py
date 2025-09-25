class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    #  dunder

    def __add__(self, other):
        print("inside add")
        # return self.x * other.x
        return self.x * other.x, self.y * other.y

    def __sub__(self, other):
        print("inside add")
        # return self.x * other.x
        return self.x - other.x, self.y - other.y

    def add(self, other):
        print("inside 2nd add")
        return self.x * other.x, self.y * other.y


a = Point(2, 4)
b = Point(3, 6)
print(a + b)
print(a - b)
