import re
from typing import List
from request_api import fetch_page
from make_the_soup import make_the_soup
from find_book_product_info import find_book_product_info
from find_book_title import find_book_title
from find_book_description import find_book_description
from find_book_category import find_book_category
from find_book_rating import find_book_rating
from find_book_image_link import find_book_image_link
from save_book_image import save_book_image


def find_all_books_infos(books_links, category_book_info: List) -> None:
    """For all the books in a list of books links in attr;
    Append info of a book to category_book_info and save image in pictures directory
    Return None

    """

    for book_link in books_links:
        page_book = fetch_page(book_link)
        soup = make_the_soup(page_book.content, 'html.parser')
        book_page_url: str = book_link
        book_product_info = find_book_product_info(soup)
        book_upc: str = book_product_info["UPC"]
        book_title = find_book_title(soup)
        print(f"\r{books_links.index(book_link)+1}/{len(books_links)}", end='')
        book_price_excl_tax_str: str = book_product_info["Price (excl. tax)"]
        book_price_excl_tax = float(book_price_excl_tax_str.replace("£", ""))
        book_price_inc_tax_str: str = book_product_info["Price (incl. tax)"]
        book_price_inc_tax = float(book_price_inc_tax_str.replace("£", ""))
        book_availaible_str: str = book_product_info["Availability"]
        match = re.search("[0-9]+", book_availaible_str)
        book_availaible = int(match.group())
        book_description = find_book_description(soup)
        book_category = find_book_category(soup)
        book_rating = find_book_rating(soup)
        book_image_link = find_book_image_link(soup)
        book_info = (
            book_page_url,
            book_upc,
            book_title,
            book_price_excl_tax,
            book_price_inc_tax,
            book_availaible,
            book_description,
            book_category,
            book_rating,
            book_image_link
        )
        category_book_info.append(book_info)
        save_book_image(book_image_link, book_category, book_upc)
    print("")
