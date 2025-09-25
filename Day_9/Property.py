# using property method

# class Alphabet:
#     def __init__(self, value):
#         self._value = value

#     def getValue(self):
#         print("Getting value")
#         return self._value

#     def setValue(self, value):
#         print("Setting value to " + value)
#         self._value = value

#     def delValue(self):
#         print("Deleting value")
#         del self._value

#     value = property(getValue, setValue, delValue)


# # Usage
# x = Alphabet("GeeksforGeeks")
# print(x.value)

# x.value = "GfG"
# del x.value


# using property Decorator
class Alphabet:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        print("Getting value from value")
        return self._value

    @value.setter
    def value(self, value):
        print("Setting value to " + value)
        if value == "Anurodh":
            self._value = value
        else:
            raise ValueError("value cannot be {value}")

    @value.getter
    def value(self):
        print("Getting value")
        return self._value

    @value.deleter
    def value(self):
        del self._value
        print("Deleting value")


# Usage
x = Alphabet("Peter")
print(x.value)

x.value = "Anurodh"
del x.value
