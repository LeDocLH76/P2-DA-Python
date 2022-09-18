from bs4 import BeautifulSoup


def find_book_title(soup: BeautifulSoup) -> str:
    """For a BeautifulSoup object of a html book page in attr,
    return the title of the book

    """

    title = soup.article.select_one("h1")
    return title.text
