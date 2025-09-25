def operators(op, num1, num2):

    match op:
        case "add":
            print(num1 + num2)
        case "sub":
            print(num1 - num2)
        case "mul":
            print(num1 * num2)
        case "div":
            print(num1 / num2)
        case "mod":
            print(num1 % num2)
        case "pow":
            print(num1**num2)
        case _:
            print("no such operator exist")


if (5 == 2) or (8 < 9):
    print(True)
else:
    print(False)

a = 2
b = 2.5
c = 2e10
print(int(a + b))
print(a + b)

s = "Best"
print(s + str(b), a, sep=" ")

print(operators(input(), int(input()), int(input())), "ans")
