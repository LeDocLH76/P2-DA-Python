from typing import List
from bs4 import BeautifulSoup

from constant import BASEURL


class Category:
    def __init__(self, page_category_soup: BeautifulSoup) -> None:
        self.set_books_links(page_category_soup)

    def set_books_links(self, page_category_soup: BeautifulSoup) -> None:
        li_list = page_category_soup.section.find_all('article')
        books_links = [li.select_one('a')['href'] for li in li_list]
        books_links = [link.replace(
            "../../..", BASEURL + "catalogue") for link in books_links]
        self._books_links = books_links
        self.set_next_page(page_category_soup)

    def add_books_links(self, page_category_soup: BeautifulSoup) -> None:
        li_list = page_category_soup.section.find_all('article')
        books_links = [li.select_one('a')['href'] for li in li_list]
        books_links = [link.replace(
            "../../..", BASEURL + "catalogue") for link in books_links]
        # print(f"Book links to add = {books_links}")
        self._books_links.extend(books_links)
        # print(f"Book links after add = {self._books_links}")
        self.set_next_page(page_category_soup)

    def set_next_page(self, page_category_soup: BeautifulSoup) -> str | None:
        try:
            self.next_page = page_category_soup.find(
                "li", class_="next").a["href"]
            print(f"Autre page à {self.next_page}")
        except AttributeError:
            print("Pas d'autre page")
            self.next_page = None

    @property
    def get_books_links(self) -> List[str]:
        return self._books_links
