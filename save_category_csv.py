import csv


def save_category_csv(category_name, category_book_info):
    """Write a .csv file for the category in attr
    Add a title line on the top

    """

    print(f"Ecriture du fichier pour la categorie : {category_name}")
    column_title = [(
        "Product_page.url",
        "UPC",
        "Title",
        "Price incl Tax £",
        "Number avalaible",
        "Product description",
        "Category",
        "Review rating /5",
        "Image.url"
    )]
    column_title.extend(category_book_info)
    with open("csv_files/" + category_name + ".csv", "w", newline='') as new_file:
        csv_writer = csv.writer(new_file)
        for line in column_title:
            csv_writer.writerow(line)
