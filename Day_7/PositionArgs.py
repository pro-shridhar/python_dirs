def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)


# Keyword-Only Arguments
"""Note: Any number of arguments in a function can have
a default value. But once we have a default argument,
all the arguments to its right must also have default values."""
nameAge(name="Prince", age=20)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`")

nameAge(age=20, name="Prince")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`")

# Positional-Only Arguments

age = 20
name = "aman"
nameAge(age, name)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`")

nameAge(name, age)
