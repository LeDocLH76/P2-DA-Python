from typing import List

from bs4 import BeautifulSoup

from constant import BASEURL


class Category():
    def __init__(
            self, page_category_soup: BeautifulSoup, category_name) -> None:
        # category_name like "historical_fiction"
        self.name = category_name
        self.set_books_links(page_category_soup)

    def set_books_links(self, page_category_soup: BeautifulSoup) -> None:
        li_list = page_category_soup.section.find_all('article')
        books_links: List[str] = [li.select_one('a')['href'] for li in li_list]
        books_links = [link.replace(
            "../../..", BASEURL + "catalogue") for link in books_links]
        self._books_links = books_links
        self.set_next_page(page_category_soup)

    def add_books_links(self, page_category_soup: BeautifulSoup) -> None:
        li_list = page_category_soup.section.find_all('article')
        books_links_to_add: List[str] = [
            li.select_one('a')['href'] for li in li_list]
        books_links_to_add = [link.replace(
            "../../..", BASEURL + "catalogue") for link in books_links_to_add]
        self._books_links.extend(books_links_to_add)
        self.set_next_page(page_category_soup)

    def set_next_page(self, page_category_soup: BeautifulSoup) -> str | None:
        try:
            self.next_page = page_category_soup.find(
                "li", class_="next").a["href"]
            # print(f"Autre page à {self.next_page}")
        except AttributeError:
            # print("Pas d'autre page")
            self.next_page = None

    @property
    def get_books_links(self) -> List[str]:
        return self._books_links
