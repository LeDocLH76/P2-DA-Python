import os


def make_category_directory(category_name: str) -> None:
    """For a category name in attr.
    Make a directory in pictures directory 
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
