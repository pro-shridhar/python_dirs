"""self is just a variable you can use any thing in place of self"""

# total_population = 100  # (1) GLOBAL variable


# class Being:

#     current_population = 0  # (2) CLASS variable

#     def __init__(self, name, age):
#         self.name = name  # INSTANCE variable
#         self.age = age
#         self.current_population += 1

#     def show_population(self):
#         current = self.current_population  # (3) LOCAL variable
#         print(
#             f"total population is = {total_population} and "
#             f"current population is = {current}"
#         )


# human = Being("Naman", 23)
# human.showPopulation()

total_population = 100  # (1) GLOBAL variable


class Being:

    current_population = 0  # (2) CLASS variable

    def __init__(this, name, age):
        this.age = age
        this.current_population += 1
        this.name = name  # INSTANCE variable

    def show_population(self):
        current = self.current_population  # (3) LOCAL variable
        print(
            f"total population is = {total_population} and "
            f"current population is = {current}"
        )

    def is_adult(self):
        self.adult = True if self.age >= 18 else False
        return self.adult


human = Being("Naman", 23)
human.show_population()
print(human.age)
