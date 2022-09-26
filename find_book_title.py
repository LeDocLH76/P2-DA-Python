from bs4 import BeautifulSoup


def find_book_title(page_book_soup: BeautifulSoup) -> str:
    """For a BeautifulSoup object of a html book page in attr,
    return the title of the book

    """

    title = page_book_soup.article.select_one("h1")
    return title.text
