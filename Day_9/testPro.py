class A:

    def __init__(self, temp):
        self._temp = temp  # Triggers the setter

    @property
    def _temp(self):
        return self.__temp  # Access the real stored value

    @_temp.setter
    def _temp(self, val):
        if val < 0:
            raise ValueError("temp can not be less than 0")
        self.__temp = val  # Avoid recursion by using a different internal name


obj = A(10)
print(obj._temp)
