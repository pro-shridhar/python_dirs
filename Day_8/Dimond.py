class Dog:
    def sound(self):
        print("Bhau Bhau")


class Cat:
    def sound(self):
        print("Meau Meau")


class Animal(Cat, Dog):
    pass


# class Animal(Dog, Cat):
#     pass
# this time Animal call Cat sound method


an = Animal()
an.sound()
