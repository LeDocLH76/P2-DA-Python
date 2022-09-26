from bs4 import BeautifulSoup


def make_the_soup(page_content, parser) -> BeautifulSoup:
    """For an HTML page and a parser in attr,
    Return a BeautifulSoup object

    """

    return BeautifulSoup(page_content, parser)
