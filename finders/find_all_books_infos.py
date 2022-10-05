import re
from typing import List
import requests
from bs4 import BeautifulSoup

from utils import make_category_directory, save_book_image
from finders.find_book_product_info import find_book_product_info
from finders.find_book_title import find_book_title
from finders.find_book_description import find_book_description
from finders.find_book_category import find_book_category
from finders.find_book_rating import find_book_rating
from finders.find_book_image_link import find_book_image_link


def find_all_books_infos(
        books_links: List[str], category_book_info: List[str]) -> None:
    """For all the books in a list of books links in attr.
    Append info of a book to category_book_info
    and save image in pictures directory
    Return None
    """

    for book_link in books_links:
        page_book = requests.get(book_link)
        page_book_soup = BeautifulSoup(page_book.content, 'html.parser')
        book_page_url = book_link
        book_product_info = find_book_product_info(page_book_soup)
        book_upc = book_product_info["UPC"]
        book_title = find_book_title(page_book_soup)
        book_category = find_book_category(page_book_soup)
        if books_links.index(book_link) == 0:
            make_category_directory(book_category)
        print(
            f"\rLivre {books_links.index(book_link)+1}/\
                {len(books_links)}", end='')
        book_price_inc_tax_str = book_product_info["Price (incl. tax)"]
        book_price_inc_tax = float(book_price_inc_tax_str.replace("£", ""))
        book_price_excl_tax_str = book_product_info["Price (excl. tax)"]
        book_price_excl_tax = float(book_price_excl_tax_str.replace("£", ""))
        book_available_str = book_product_info["Availability"]
        # book_available_str like: In stock (19 available)
        match = re.search("[0-9]+", book_available_str)
        book_available = int(match.group())
        book_description = find_book_description(page_book_soup)
        book_rating = find_book_rating(page_book_soup)
        book_image_link = find_book_image_link(page_book_soup)
        book_info = (
            book_page_url,
            book_upc,
            book_title,
            book_price_inc_tax,
            book_price_excl_tax,
            book_available,
            book_description,
            book_category,
            book_rating,
            book_image_link
        )
        category_book_info.append(book_info)
        save_book_image(book_image_link, book_category, book_upc)
    print("")
