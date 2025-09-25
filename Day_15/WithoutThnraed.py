import threading
import time
import os
import requests
import uuid

thread_local = threading.local()


def main():
    sites = "https://raw.githubusercontent.com/avinchhibestpeers/Bottle-image-links/refs/heads/main/img.txt"

    if not os.path.exists("images1"):
        os.mkdir("images1")

    start_time = time.perf_counter()
    download_site(sites)
    duration = time.perf_counter() - start_time
    print(f"Downloaded images in {duration:.2f} seconds")


def download_site(url):
    session = get_session_for_thread()
    response = session.get(url)
    if response.status_code == 200:
        image_urls = [
            line.strip() for line in response.text.splitlines() if line.strip()
        ]
        download_images(image_urls)
    else:
        print(f"Failed to fetch image URL list. Status code: {response.status_code}")


def download_images(url_list):
    for url in url_list:
        download_image(url)


def download_image(url):
    myuuid = str(uuid.uuid4()) + ".jpg"
    try:
        response = requests.get(url, stream=True, timeout=10)
        if response.ok:
            with open(f"images1/{myuuid}", "wb") as handle:
                for block in response.iter_content(1024):
                    if block:
                        handle.write(block)
            print(f"Downloaded: {url}")
        else:
            print(f"Failed to download {url} - Status code: {response.status_code}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")


def get_session_for_thread():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


if __name__ == "__main__":
    main()
