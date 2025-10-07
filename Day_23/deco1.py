import time
import functools


def slow_down(func):
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)

    return wrapper_slow_down


@slow_down
def say_hello():
    """Say hello."""
    print("Hello!")


print(say_hello.__name__)  # say_hello
print(say_hello.__doc__)  # Say hello.
