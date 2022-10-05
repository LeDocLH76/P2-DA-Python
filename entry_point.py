"""Module for extracting books's data on web site"""
import time
from typing import List

from constant import BASEURL
from request_api import fetch_page
from make_the_soup import make_the_soup
from find_category_books_links import find_category_books_links
from find_all_books_infos import find_all_books_infos
from save_category_csv import save_category_csv


def main():
    """Get books infos on https://books.toscrape.com
    and save them by categories in csv files.
    Get books's images and save them in a directory for each category of book.
    """
    start = time.time()
    main_page = fetch_page(BASEURL+"index.html")
    main_page_soup = make_the_soup(main_page.content, 'html.parser')
    # Find categories links in the main page
    li_list = main_page_soup.aside.ul.ul.find_all("li")
    categories_links: List[str] = [
        BASEURL + li.select_one('a')['href'] for li in li_list]

    for category_link in categories_links:
        books_links = find_category_books_links(category_link)
        # category_link like: catalogue/category/books/travel_2/index.html
        category_name = category_link.split("/")[-2]
        category_name = category_name.split("_")[0]
        # category_name like: historical-fiction
        print(
            f"Catégorie {categories_links.index(category_link)+1}/\
{len(categories_links)}")
        category_book_info = []
        find_all_books_infos(books_links, category_book_info)
        save_category_csv(category_name, category_book_info)
    print("Travail terminé")

    end = time.time()
    duree = round(end - start)
    minute = duree // 60
    seconde = duree % 60
    print(f"Temps d'execution = {minute}  minutes {seconde} secondes")


if __name__ == "__main__":
    main()
