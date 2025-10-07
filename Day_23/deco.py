import time


def slow_down(func):
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)

    return wrapper_slow_down


@slow_down
def say_hello():
    """Say hello."""
    print("Hello!")


print(say_hello.__name__)  # wrapper_slow_down
print(say_hello.__doc__)  # None
