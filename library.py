from typing import List

from request_api import fetch_page
from make_the_soup import make_the_soup


class Library:
    def __init__(self, base_url) -> None:
        self.base_url = base_url
        self.site_url = f"{base_url}index.html"
        # print(f"Library init, site url = {self.site_url}")
        self.categories, self.categories_names = Library.find_categories_links(
            self)

    def find_categories_links(self) -> List[str]:
        page_main = fetch_page(self.site_url)
        page_main_soup = make_the_soup(page_main.content, "html.parser")
        li_list = page_main_soup.aside.ul.ul.find_all("li")
        categories_links = [
            self.base_url + li.select_one('a')['href'] for li in li_list]
        categories_names = [
            li.select_one('a').text.strip().replace(" ", "_").lower()
            for li in li_list]

        return categories_links, categories_names
