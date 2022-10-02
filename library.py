from typing import List

from bs4 import ResultSet

from constant import BASEURL


class Library:
    def __init__(self, page_main_soup: ResultSet) -> None:
        self.set_categories_links(page_main_soup)
        self.set_categories_names(page_main_soup)
        # print(f"Library init, site url = {self.site_url}")

    def set_categories_links(self, page_main_soup) -> None:
        li_list = page_main_soup.aside.ul.ul.find_all("li")
        self._categories_links: List[str] = [
            BASEURL + li.select_one('a')['href'] for li in li_list]

    def set_categories_names(self, page_main_soup) -> None:
        li_list = page_main_soup.aside.ul.ul.find_all("li")
        self._categories_names: List[str] = [
            li.select_one('a').text.strip().replace(" ", "_").lower()
            for li in li_list]

    @property
    def get_categories_links(self) -> List[str]:
        return self._categories_links

    @property
    def get_categories_names(self) -> List[str]:
        return self._categories_names
