def arithmetic_operation(str: str) -> int:
    arr = str.split()

    option = arr[1]
    num1 = int(arr[0])
    num2 = int(arr[2])

    match option:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "//":
            if num2 == 0:
                return -1
            return num1 // num2
        case _:
            return -1
