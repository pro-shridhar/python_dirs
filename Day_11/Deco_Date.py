import time


def deco(fun):
    def wapper():
        start_time = time.time()
        print(start_time)
        fun()
        end_time = time.time()
        print(f"{(end_time - start_time):.2f}")

    return wapper


def deco1(fun):

    def wapper():

        print("befor")
        fun()
        print("after")

    return wapper


@deco1
@deco
def run():
    for i in range(100000000):
        pass


@deco
def run1():
    for i in range(2000000):
        pass


# run()
run1()
