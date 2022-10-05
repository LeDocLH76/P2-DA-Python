from typing import List
from bs4 import BeautifulSoup

from constant import BASEURL


def find_page_books_links(page_category_soup: BeautifulSoup) -> List[str]:
    """For a BeautifulSoup object of a html category page in attr,
    return list of books links

    """

    li_list = page_category_soup.section.find_all('article')
    books_links = [li.select_one('a')['href'] for li in li_list]
    books_links = [link.replace(
        "../../..", BASEURL + "catalogue") for link in books_links]
    return books_links
