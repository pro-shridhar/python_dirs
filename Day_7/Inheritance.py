"""Global variables are declared outside all functions
and can be accessed anywhere in the program,
including inside functions."""

"""Local variables are created inside a function
and exist only during its execution. They cannot
be accessed from outside the function."""


class Car:

    # class variable
    car_type = "super car"

    def car_dis(self):
        print(self.car_type)


class Bike:

    bike_type = "EV bikes"

    def car_dis(self):
        print(self.bike_type)


class Bugatti(Car):

    def __init__(self, rate, average):
        # instance variables
        self.rate = rate
        self.average = average

    def name_of_car(self):
        print("name = Bugatti", self.car_type, self.average, self.rate)


class Chiron(Bugatti):

    def model(self):
        print(
            f"name = Bugatti Chiron, type = {self.car_type}, "
            f"average = {self.average}, rate = {self.rate}"
        )


class Vehicle(Car, Bike):

    def vehicle_type(self):
        print(f"car type is {Car.car_type} bike type is {Bike.bike_type}")


chiron = Chiron("20 Million", 5)
vehicle = Vehicle()

chiron.model()
vehicle.vehicle_type()
