from typing import List
from bs4 import BeautifulSoup
from constant import BASEURL


def find_categories_links(soup: BeautifulSoup) -> List[str]:
    """For a BeautifulSoup object of the html main page in attr,
    return a list of links for the categories 

    """

    li_list = soup.aside.ul.ul.find_all("li")
    categories_links = [BASEURL + li.select_one('a')['href'] for li in li_list]
    return categories_links
