class Dog:
    obj_count = 0

    def __init__(self):
        Dog.obj_count += 1


dog = Dog()
dog1 = Dog()
print(Dog.obj_count)
