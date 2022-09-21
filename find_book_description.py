from bs4 import BeautifulSoup


def find_book_description(soup: BeautifulSoup) -> str:
    """For a BeautifulSoup object of a html book page in attr,
    return the description of the book

    """
    try:
        description = soup.article.find(
            id="product_description").next_sibling.next_sibling.text
        return description
    except AttributeError:
        return "Description manquante"
