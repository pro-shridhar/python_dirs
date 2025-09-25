def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


operation_map = {
    "add": add,
    "sub": sub,
    "mul": mul,
    "div": div,
}


def calculate(op, x, y):
    func = operation_map.get(op)
    if not func:
        raise ValueError("Invalid operation")
    return func(x, y)


print(calculate("add", 4, 7))
