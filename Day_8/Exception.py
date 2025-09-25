"""if there is zero then ZeroDivision error block exicute
if there is any number thrn else exicute
finally exicute every time"""

try:
    n = 1
    res = 100 / n

except ZeroDivisionError:
    print("You can't divide by zero!")

except ValueError:
    print("Enter a valid number!")

else:
    print("Result is", res)

finally:
    print("Execution complete.")

locals()["__builtins__"]

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def set(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age set to {age}")


try:
    set(-5)
except ValueError as e:
    print(e)
