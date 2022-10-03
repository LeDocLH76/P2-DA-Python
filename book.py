import re
from typing import List

from constant import BASEURL, RATINGVALUES


class Book:
    def __init__(self, page_book_soup, page_book_url, category_name) -> None:
        self._page_url = page_book_url
        # Like "historical_fiction"
        self._category = category_name
        self._product_info = self.product_info(page_book_soup)
        self.set_title(page_book_soup)
        self.set_price_inc_tax()
        self.set_price_excl_tax()
        self._upc = self._product_info["UPC"]
        self.set_available()
        self.set_description = self.set_description(page_book_soup)
        self.set_rating = self.set_rating(page_book_soup)
        self.set_image_link = self.set_image_link(page_book_soup)

    def set_title(self, page_book_soup) -> str:
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

    def set_description(self, page_book_soup) -> None:
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

    def set_rating(self, page_book_soup) -> None:
        rating = page_book_soup.select_one(".star-rating")['class']
        rating = RATINGVALUES[rating[1]]
        self._rating = rating

    def set_image_link(self, page_book_soup) -> None:
        link = page_book_soup.select_one(".carousel-inner img")['src']
        link = link.replace("../..", BASEURL)
        self._image_link = link

    @property
    def get_book_info(self) -> List[str | int | float]:
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
    def product_info(page_book_soup) -> dict:
        # With in key:
        # - UPC
        # - Product Type
        # - Price (excl. tax)
        # - Price (incl. tax)
        # - Tax
        # - Availability
        # - Number of reviews

        table_key = page_book_soup.table.find_all("th")
        table_key = [key.text for key in table_key]
        table_value = page_book_soup.table.find_all("td")
        table_value = [value.text for value in table_value]
        product_info = dict(zip(table_key, table_value))
        return product_info
