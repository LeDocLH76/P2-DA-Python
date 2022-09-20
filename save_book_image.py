import os
import requests


def save_book_image(url: str, upc: str) -> None:
    """Save image from the url in attr in pictures directory"""

    page = requests.get(url)
   #  print(f"Status = {page.status_code}")
    file_extention = os.path.splitext(url)[-1]
    with open("pictures/" + upc + file_extention, "wb") as f:
        f.write(page.content)


if __name__ == "__main__":
    save_book_image(
        "https://books.toscrape.com/media/cache/fe/72/fe72f0532301ec28892ae79a629a293c.jpg", "upc_test")
