class CustomEcxeptionError(Exception):

    def __init__(self, message, error_code):
        self.message = message
        self.error_code = error_code
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"


def divide(a, b):

    if b == 0:
        raise CustomEcxeptionError("Division by zero is not allowed", 400)
    return a / b


try:
    # result = divide(10, 0)
    raise CustomEcxeptionError("sample exception", 401)
except CustomEcxeptionError as e:
    print(f"Caught an error: {e}")
