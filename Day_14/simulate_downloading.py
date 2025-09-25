import threading
import random
import time


def download():

    print("-----", end="", flush=True)


def main_task():

    t1 = threading.Thread(target=download)

    t1.start()

    t1.join()


print("downloading start...")
for i in range(10):
    main_task()
    sec = random.randint(1, 2)
    time.sleep(sec)
print("downloading complete")
