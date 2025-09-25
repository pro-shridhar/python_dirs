import threading
import time
from concurrent.futures import ThreadPoolExecutor
import os
import requests
import uuid

thread_local = threading.local()


def main():
    sites = "https://raw.githubusercontent.com/avinchhibestpeers/Bottle-image-links/refs/heads/main/img.txt"
    start_time = time.perf_counter()
    download_site(sites)
    duration = time.perf_counter() - start_time
    print(f"Downloaded {len(sites)} sites in {duration} seconds")


def download_site(url):
    session = get_session_for_thread()
    with session.get(url) as response:
        # img_data = response.content

        # with open("image_url.txt", "wb") as image_url:
        #     image_url.write(img_data)

        if response.status_code == 200:
            image_urls = [
                line.strip() for line in response.text.splitlines() if line.strip()
            ]
            download_images(image_urls)


def download_images(url):
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_image, url)


os.mkdir("images")


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


def get_session_for_thread():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


if __name__ == "__main__":
    main()
