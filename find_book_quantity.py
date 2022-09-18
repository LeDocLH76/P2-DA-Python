from bs4 import BeautifulSoup


def find_book_quantity(soup: BeautifulSoup) -> int:
    """For a BeautifulSoup object of a category html page in attr,
    return the number of the books in category

    """

    book_quantity = int(soup.form.find("strong").text)
    return book_quantity
