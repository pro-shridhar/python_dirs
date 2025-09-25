import multiprocessing


def cube(my_list, q):

    for i in my_list:
        q.put(i**3)


def show(q):

    print("queue element")
    while not q.empty():
        print(q.get())
    print("Queue is now empty!")


if __name__ == "__main__":

    my_list = [2, 3, 4, 5]

    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(
        target=cube,
        args=(
            my_list,
            q,
        ),
    )
    p2 = multiprocessing.Process(target=show, args=(q,))

    p1.start()
    p1.join()

    p2.start()
    p2.join()
