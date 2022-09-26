import csv


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
    column_title.extend(category_book_info)
    with open("csv_files/" + category_name + ".csv", "w", encoding="utf-8", newline='') as new_file:
        csv_writer = csv.writer(new_file)
        for line in column_title:
            csv_writer.writerow(line)
