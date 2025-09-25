import multiprocessing


def cube(num):

    print("cube of a number", num**3)


def square(num):

    print("square of a number", num**2)


if __name__ == "__main__":

    p1 = multiprocessing.Process(target=cube, args=(5,))
    p2 = multiprocessing.Process(target=square, args=(5,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done!")
