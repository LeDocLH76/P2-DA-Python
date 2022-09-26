import os
import requests


def save_book_image(url: str, category_name: str, upc: str) -> None:
    """Save image from the url in attr in pictures/category directory"""
    category_name = category_name.replace(" ", "_")
    page = requests.get(url)
   #  print(f"Status = {page.status_code}")
    file_extention = os.path.splitext(url)[-1]
    with open("pictures/" + category_name + "/" + upc + file_extention, "wb") as f:
        f.write(page.content)
