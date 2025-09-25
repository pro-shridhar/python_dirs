import requests


def download_image(url):

    with open("pic1.jpg", "wb") as handle:
        response = requests.get(url, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            # myuuid = uuid.uuid4()
            handle.write(block)


url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQEBgJ0Gq3Voun-1v6N4C2fl-t4LY2uB3XAvg&s"


download_image(url)
