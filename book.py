import re
from typing import List, Tuple

from bs4 import BeautifulSoup

from constant import BASEURL, RATINGVALUES


class Book:
    def __init__(self, page_book_soup: BeautifulSoup,
                 page_book_url: str,
                 category_name: str) -> None:
        self._page_url = page_book_url
        # category_name like "historical_fiction"
        self._category = category_name
        self._product_info = self.product_info(page_book_soup)
        self.set_title(page_book_soup)
        self.set_price_inc_tax()
        self.set_price_excl_tax()
        self._upc: str = self._product_info["UPC"]
        self.set_available()
        self.set_description(page_book_soup)
        self.set_rating(page_book_soup)
        self.set_image_link(page_book_soup)

    def set_title(self, page_book_soup: BeautifulSoup) -> str:
        title = page_book_soup.article.select_one("h1").text
        self._title = title

    def set_price_inc_tax(self) -> None:
        price_inc_tax_str: str = self._product_info[
            "Price (incl. tax)"]
        price_inc_tax = float(price_inc_tax_str.replace("£", ""))
        self._price_inc_tax = price_inc_tax

    def set_price_excl_tax(self) -> None:
        price_excl_tax_str: str = self._product_info[
            "Price (excl. tax)"]
        price_excl_tax = float(price_excl_tax_str.replace("£", ""))
        self._price_excl_tax = price_excl_tax

    def set_available(self) -> None:
        available_str: str = self._product_info["Availability"]
        # book_available_str like: In stock (19 available)
        match = re.search("[0-9]+", available_str)
        available = int(match.group())
        self._available = available

    def set_description(self, page_book_soup: BeautifulSoup) -> None:
        try:
            description = page_book_soup.article.find(
                id="product_description").next_sibling.next_sibling.text
            self._description = description
        except AttributeError:
            self._description = "Missing description"

    # def set_category(self, page_book_soup) -> None:
    #     category = page_book_soup.ul.find(
    #         class_="active").previous_sibling.previous_sibling.text
    #     # category like: Historical Fiction
    #     category = category.replace("\n", "")
    #     self._category = category

    def set_rating(self, page_book_soup: BeautifulSoup) -> None:
        rating_str: str = page_book_soup.select_one(".star-rating")['class']
        rating: int = RATINGVALUES[rating_str[1]]
        self._rating = rating

    def set_image_link(self, page_book_soup: BeautifulSoup) -> None:
        link: str = page_book_soup.select_one(".carousel-inner img")['src']
        link = link.replace("../..", BASEURL)
        self._image_link = link

    @property
    def get_book_info(self) -> Tuple[
            str, str, str, float, float, int, str, str, int, str]:
        info = (
            self._page_url,
            self._upc,
            self._title,
            self._price_inc_tax,
            self._price_excl_tax,
            self._available,
            self._description,
            self._category,
            self._rating,
            self._image_link)
        return info

    @staticmethod
    def product_info(page_book_soup: BeautifulSoup) -> dict[str, str]:
        # With in key:
        # - UPC
        # - Product Type
        # - Price (excl. tax)
        # - Price (incl. tax)
        # - Tax
        # - Availability
        # - Number of reviews

        table_key: List[str] = page_book_soup.table.find_all("th")
        table_key = [key.text for key in table_key]
        table_value: List[str] = page_book_soup.table.find_all("td")
        table_value = [value.text for value in table_value]
        product_info = dict(zip(table_key, table_value))
        return product_info
