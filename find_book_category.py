from bs4 import BeautifulSoup


def find_book_category(page_book_soup: BeautifulSoup) -> str:
    """For a BeautifulSoup object of a html book page in attr,
    return the category name of the book

    """

    category = page_book_soup.ul.find(
        class_="active").previous_sibling.previous_sibling.text
    # category like: Historical Fiction
    category = category.replace("\n", "")
    return category
