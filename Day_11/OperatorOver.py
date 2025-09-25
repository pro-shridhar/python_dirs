class A:

    def __init__(self):
        self.name = self.__class__.__name__

    def __and__(self, other):
        return self.name + other.name

    def __len__(self, other):
        return len(self.name) + len(other.name)


a = A()
b = A()


print(a & b)
print(a.__len__(b))
