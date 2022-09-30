import re

from constant import BASEURL, RATINGVALUES
from make_the_soup import make_the_soup
from request_api import fetch_page


class Book:
    def __init__(self, book_page_url) -> None:
        self.book_page_url = book_page_url
        self.book_soup = Book.find_book_soup(self)
        self.book_product_info = Book.find_book_product_info
        self.book_upc = self.book_product_info["UPC"]
        # --self.book_title
        # --self.book_price_inc_tax
        # --self.book_price_excl_tax
        # --self.book_available
        # --self.book_description
        # --self.book_category
        # --self.book_rating
        # --self.book_image_link

    def find_book_soup(self):
        page_book = fetch_page(self.book_page_url)
        page_book_soup = make_the_soup(page_book.content, 'html.parser')
        return page_book_soup

    def find_book_product_info(self) -> dict:
        # With in key:
        # - UPC
        # - Product Type
        # - Price (excl. tax)
        # - Price (incl. tax)
        # - Tax
        # - Availability
        # - Number of reviews

        table_key = self.book_soup.table.find_all("th")
        table_key = [key.text for key in table_key]
        table_value = self.book_soup.table.find_all("td")
        table_value = [value.text for value in table_value]
        product_info = dict(zip(table_key, table_value))
        return product_info

    @property
    def find_book_title(self) -> str:
        title = self.book_soup.article.select_one("h1")
        return title.text

    @property
    def book_category(self) -> str:
        category = self.book_soup.ul.find(
            class_="active").previous_sibling.previous_sibling.text
        # category like: Historical Fiction
        category = category.replace("\n", "")
        return category

    @property
    def book_description(self) -> str:
        try:
            description = self.book_soup.article.find(
                id="product_description").next_sibling.next_sibling.text
            return description
        except AttributeError:
            return "Missing description"

    @property
    def find_book_rating(self) -> int:
        rating = self.book_soup.select_one(".star-rating")['class']
        rating = RATINGVALUES[rating[1]]
        return rating

    @property
    def find_book_image_link(self) -> str:
        link = self.book_soup.select_one(".carousel-inner img")['src']
        link = link.replace("../..", BASEURL)
        return link

    @property
    def book_price_inc_tax(self):
        book_price_inc_tax_str: str = Book.book_product_info[
            "Price (incl. tax)"]
        book_price_inc_tax = float(book_price_inc_tax_str.replace("£", ""))
        return book_price_inc_tax

    @property
    def book_price_excl_tax(self):
        book_price_excl_tax_str: str = Book.book_product_info[
            "Price (excl. tax)"]
        book_price_excl_tax = float(book_price_excl_tax_str.replace("£", ""))
        return book_price_excl_tax

    @property
    def book_available(self):
        book_available_str: str = Book.book_product_info["Availability"]
        # book_available_str like: In stock (19 available)
        match = re.search("[0-9]+", book_available_str)
        book_available = int(match.group())
        return book_available
