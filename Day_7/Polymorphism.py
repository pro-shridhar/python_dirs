# Polymorphism

"""Run-Time Polymorphism:

-> Demonstrated using method overriding in the Dog class and
its subclasses (Labrador and Beagle).
-> The correct sound method is invoked at runtime based on the
actual type of the object in the list.

2. Compile-Time Polymorphism:

-> Python does not natively support method overloading. Instead,
we use a single method (add) with default arguments to handle
varying numbers of parameters.
-> Different behaviors (adding two or three numbers) are
achieved based on how the method is called.
"""


class Add:

    def add(self, a, b=0, c=0):  # method overloading or compile time
        print(a + b + c)


class Operation(Add):

    def add(self, a, b=0, c=0):  # method overriding or run time
        return a + b + c


add = Add()
print("method overloading or compile time polymorphism")
add.add(4, 5, 6)
add.add(4, 6)

op = Operation()
print("method overriding or run time polymorphism")
print(op.add(7, 8))
