"""Module for extracting books's data on web site"""
from constant import BASEURL
from request_api import fetch_page
from make_the_soup import make_the_soup
from find_categories_links import find_categories_links
from find_category_books_links import find_category_books_links
from find_all_books_infos import find_all_books_infos
from save_category_csv import save_category_csv


def main():
    """Get books infos on https://books.toscrape.com
    and save them by categories in csv files.
    Get books's images and save them in a directory for each category of book.
    """
    page_base = fetch_page(BASEURL+"index.html")
    soup = make_the_soup(page_base.content, 'html.parser')
    categories_links = find_categories_links(soup)
    for category_link in categories_links:
        category_link: str = category_link
        books_links = find_category_books_links(category_link)
        # category_link like: catalogue/category/books/travel_2/index.html
        category_name = category_link.split("/")[-2]
        # category_name like: travel_2
        category_name = category_name.split("_")[0]
        print(
            f"Catégorie {categories_links.index(category_link)+1}/\
                {len(categories_links)}")
        category_book_info = []
        find_all_books_infos(books_links, category_book_info)
        save_category_csv(category_name, category_book_info)
    print("Travail terminé")


if __name__ == "__main__":
    main()
