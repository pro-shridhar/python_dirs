def fun(cls):
    print("befor")
    cls.class_name = cls.__name__
    cls._class = cls.prt(cls)
    print("after")
    return cls


@fun
class Person:

    def prt(self):
        print("print")


obj = Person("Admin")
print(obj.prt())
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print(Person.class_name)
