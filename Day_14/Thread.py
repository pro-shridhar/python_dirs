import threading
import time


def fun(name):

    for i in range(10):
        print(f"{name} start", i)
        time.sleep(1)
    # print(f"{name} end")


thread1 = threading.Thread(target=fun, args=("thread1",))
thread2 = threading.Thread(target=fun, args=("thread2",))
thread3 = threading.Thread(target=fun, args=("thread3",))

thread1.start()
thread2.start()
thread3.start()

"""main methodeis also a thread so if we not use
join then main method exicute before threads"""
thread1.join()
thread2.join()


print("work has done")
