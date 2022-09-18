from bs4 import BeautifulSoup
from constant import BASEURL


def find_book_image_link(soup: BeautifulSoup) -> str:
    """For a BeautifulSoup object of a html book page in attr,
    return the image link of the book

    """

    link = soup.select_one(".carousel-inner img")['src']
    link = link.replace("../..", BASEURL)
    return link
