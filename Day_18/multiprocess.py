from concurrent.futures import ProcessPoolExecutor
import time


def process():

    for i in range(10000):
        pass

    return


if __name__ == "__main__":
    t1 = time.time()
    with ProcessPoolExecutor(max_workers=10) as exe:
        exe.submit(process, range(10000))
    t2 = time.time() - t1
    print(t2)

    t1 = time.time()
    for i in range(10000):
        process()

    t2 = time.time() - t1
    print(t2)
