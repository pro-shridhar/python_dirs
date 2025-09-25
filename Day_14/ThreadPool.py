import threading
import time
from concurrent.futures import ThreadPoolExecutor

import requests

thread_local = threading.local()


def main():
    sites = (
        "https://raw.githubusercontent.com/avinchhibestpeers/Bottle-image-links/refs/heads/main/img.txt",
    )
    start_time = time.perf_counter()
    download_site(sites)
    duration = time.perf_counter() - start_time
    print(f"Downloaded {len(sites)} sites in {duration} seconds")


def download_all_sites(sites):
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)


def download_site(url):
    session = get_session_for_thread()
    with session.get(url) as response:
        img_data = response.content

        with open("image_name.txt", "wb") as handler:
            handler.write(img_data)


def get_session_for_thread():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


if __name__ == "__main__":
    main()
