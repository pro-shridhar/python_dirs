"""Another way to achieve polymorphism besides Inheritance
Object must have the minimum necessary attributes/methods
'if it look like a duck and quacks like a duck, it must be duck'"""


class Birds:
    alive = True

    def discribe(self):
        print("they can fly")


class Egle(Birds):
    pass


class Sperrow(Birds):
    pass


class Airoplain:

    alive = True

    def discribe(self):
        print("they can fly")


for obj in Egle(), Sperrow(), Airoplain():
    obj.discribe()
    print(obj.alive)
