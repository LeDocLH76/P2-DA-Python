import csv


def save_category_csv(category_name, category_book_info):
    print("Ici est sauvegardé le fichier")
    print(f"La categorie est : {category_name}")
    print(f"La longueur est : {len(category_book_info)}")
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
    # print(*column_title, sep="\n")
    with open("csv_files/" + category_name + ".csv", "w", newline='') as new_file:
        csv_writer = csv.writer(new_file)
        for line in column_title:
            csv_writer.writerow(line)
