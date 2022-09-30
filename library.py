from typing import List

from bs4 import ResultSet

from constant import BASEURL
from request_api import fetch_page
from make_the_soup import make_the_soup


class Library:
    def __init__(self, base_url) -> None:
        self.site_url = f"{base_url}index.html"
        # print(f"Library init, site url = {self.site_url}")

    @property
    def categories_links(self) -> List[str]:
        li_list = Library.find_li_list(self)
        categories_links = [
            BASEURL + li.select_one('a')['href'] for li in li_list]
        return categories_links

    @property
    def categories_names(self) -> List[str]:
        li_list = Library.find_li_list(self)
        categories_names = [
            li.select_one('a').text.strip().replace(" ", "_").lower()
            for li in li_list]
        return categories_names

    def find_li_list(self) -> ResultSet:
        page_main = fetch_page(self.site_url)
        page_main_soup = make_the_soup(page_main.content, "html.parser")
        li_list = page_main_soup.aside.ul.ul.find_all("li")
        return li_list
