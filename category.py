from typing import List

from bs4 import BeautifulSoup

from constant import BASEURL
from request_api import fetch_page
from make_the_soup import make_the_soup


class Category:
    def __init__(self, category_url: str) -> None:
        self.category_url = category_url

    @property
    def name(self) -> str:
        # category_link like: catalogue/category/books/travel_2/index.html
        category_name = self.category_url.split("/")[-2]
    # category_name like: travel_2
        category_name = category_name.split("_")[0]
        return category_name

    @property
    def books_url(self) -> List[str]:
        page_category = fetch_page(self.category_url)
        category_soup: BeautifulSoup = make_the_soup(
            page_category.content, "html.parser")
        category_total_page_quantity = Category.find_page_quantity(
            category_soup)
        # Find the books links for the first page
        books_links = Category.find_page_books_links(category_soup)
        # Find the books links for the other pages
        for page in range(category_total_page_quantity-1):
            page_offset = str(page + 2)
            # construct the end part of the next page url
            next_page = "page-" + page_offset + ".html"
            split_url = self.category_url.split("/")
            # Replace the end of the url
            split_url[-1] = next_page
            next_url = "/".join(split_url)
            next_page_category = fetch_page(next_url)
            next_page_category_soup = make_the_soup(
                next_page_category.content, 'html.parser')
            books_links_to_add = Category.find_page_books_links(
                next_page_category_soup)
            books_links.extend(books_links_to_add)
        return books_links

    @staticmethod
    def find_page_quantity(category_soup: BeautifulSoup) -> int:
        category_books_quantity = Category.find_book_quantity(category_soup)
        category_full_page_quantity = category_books_quantity // 20
        category_last_page_quantity = int(0)
        if category_books_quantity % 20 != 0:
            category_last_page_quantity = int(1)
        category_total_page_quantity = \
            category_full_page_quantity + category_last_page_quantity
        return category_total_page_quantity

    @staticmethod
    def find_book_quantity(category_soup: BeautifulSoup) -> int:
        book_quantity = int(category_soup.form.find("strong").text)
        return book_quantity

    @staticmethod
    def find_page_books_links(category_soup: BeautifulSoup) -> List[str]:
        li_list = category_soup.section.find_all('article')
        books_links = [li.select_one('a')['href'] for li in li_list]
        books_links = [link.replace(
            "../../..", BASEURL + "catalogue") for link in books_links]
        return books_links
