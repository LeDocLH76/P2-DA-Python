import time
from typing import List
from book import Book

from constant import BASEURL
from library import Library
from category import Category
from request_api import fetch_page
from make_the_soup import make_the_soup
from make_category_directory import make_category_directory
from save_book_image import save_book_image
from save_category_csv import save_category_csv


start = time.time()

# *********************
# Search for categories
# *********************
site_url = f"{BASEURL}index.html"
page_main = fetch_page(site_url)
page_main_soup = make_the_soup(page_main.content, "html.parser")
library = Library(page_main_soup)

# *********************
# Search for books
# *********************
categories_obj: List[Category] = []
for url_to_fetch, category_name in zip(
        library.get_categories_links, library.get_categories_names):

    if category_name == "historical_fiction":
        break

    # category_name like "historical_fiction"
    page_category = fetch_page(url_to_fetch)
    page_category_soup = make_the_soup(page_category.content, "html.parser")

    categories_obj.append(Category(page_category_soup, category_name))
    category_obj_index = categories_obj[library.get_categories_links.index(
        url_to_fetch)]

    while category_obj_index.next_page is not None:
        # unbuild the category first page url and remove the end
        next_page_url = url_to_fetch.split("/")[:-1]
        # add a new end
        next_page_url.append(category_obj_index.next_page)
        # build the category next page url
        next_page_url = "/".join(next_page_url)

        page_category = fetch_page(next_page_url)
        page_category_soup = make_the_soup(
            page_category.content, "html.parser")

        category_obj_index.add_books_links(page_category_soup)

    livre_s = "livre" if len(
        category_obj_index.get_books_links) < 2 else "livres"
    print(
        f"Récupération de la catégorie \
{library.get_categories_links.index(url_to_fetch)+1}/\
{len(library.get_categories_links)} {category_name}, \
et des liens pour {len(category_obj_index.get_books_links)} {livre_s}")

# *********************
# Search for books infos
# *********************
books_obj: List[Book] = []
for category_link, category_name in zip(
        library.get_categories_links, library.get_categories_names):
    # category_name like "historical_fiction"

    if category_name == "historical_fiction":
        break

    books_links = categories_obj[library.get_categories_links.index(
        category_link)].get_books_links
    for url_to_fetch in books_links:
        page_book = fetch_page(url_to_fetch)
        page_book_soup = make_the_soup(page_book.content, "html.parser")
        books_obj.append(Book(page_book_soup, url_to_fetch, category_name))

    livre_s = "livre" if len(
        books_links) < 2 else "livres"
    print(f"Récupération des infos de \
{len(books_links)} {livre_s} dans la catégorie \
{library.get_categories_links.index(category_link)+1}/\
{len(library.get_categories_links)}")


print(f"Nombre de livre = {len(books_obj)}")

# *********************
# Save categories.csv
# Save images
# *********************
for category_obj in categories_obj:
    category_name = category_obj.name
    # category_name like "historical_fiction"
    make_category_directory(category_name)
    books_info_in_category = []
    for book_obj in books_obj:
        if book_obj.get_book_info[7] == category_name:
            books_info_in_category.append(book_obj.get_book_info)
            save_book_image(
                book_obj.get_book_info[0],
                book_obj.get_book_info[7],
                book_obj.get_book_info[1])
    save_category_csv(category_name, books_info_in_category)

end = time.time()
duree = (end - start)/1000
print(f"Temps d'execution = {duree:.2} secondes")
