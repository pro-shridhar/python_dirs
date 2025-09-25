import threading
from concurrent.futures import ThreadPoolExecutor
import uuid


import requests

thread_local = threading.local()


def travers():

    with open("image_name.txt", "r") as image_url:
        image_file = list(image_url.read())
        download_images(image_file)


def download_images(url):
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_image, url)


def download_image(url):

    myuuid = str(uuid.uuid4()) + ".jpg"

    with open(f"images/{myuuid}", "wb") as handle:
        response = requests.get(url, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)


travers()
