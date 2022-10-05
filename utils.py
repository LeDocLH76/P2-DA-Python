import os
import requests
import csv


def make_category_directory(category_name: str) -> None:
    """For a category name in attr. make a directory in pictures directory \
        with the formated category_name
    """
    # category_name like: Historical Fiction
    category_name = category_name.replace(" ", "_")
    try:
        os.mkdir("pictures/" + category_name)
        # print("Création")
    except FileExistsError:
        # print("Le repertoire existe déja")
        pass


def save_book_image(image_url: str, category_name: str, book_upc: str) -> None:
    """Save image from the url in attr in pictures/category directory"""
    category_name = category_name.replace(" ", "_")
    page = requests.get(image_url)
    #  print(f"Status = {page.status_code}")
    file_extention = os.path.splitext(image_url)[-1]
    with open(
        "pictures/" + category_name + "/" + book_upc + file_extention, "wb"
    ) as f:
        f.write(page.content)


def save_category_csv(category_name, category_book_info) -> None:
    """Write a .csv file for the category in attr
    Add a title line on the top
    """
    print(f"Ecriture du fichier pour la categorie : {category_name}")
    column_title = [(
        "product_page_url",
        "universal_product_code",
        "title",
        "price_including_tax",
        "price_excluding_tax",
        "number_avalaible",
        "product_description",
        "category",
        "review_rating",
        "image_url"
    )]
    with open("csv_files/" + category_name + ".csv",
              "w", encoding="utf-8", newline='') as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerow(column_title)
        for line in category_book_info:
            csv_writer.writerow(line)
