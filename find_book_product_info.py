from bs4 import BeautifulSoup


def find_book_product_info(page_book_soup: BeautifulSoup) -> dict:
    """For a BeautifulSoup object of a book html page in attr,
    return dictionnary of book info.

    With in key:
    - UPC
    - Product Type
    - Price (excl. tax)
    - Price (incl. tax)
    - Tax
    - Availability
    - Number of reviews

    """

    table_key = page_book_soup.table.find_all("th")
    table_key = [key.text for key in table_key]
    table_value = page_book_soup.table.find_all("td")
    table_value = [value.text for value in table_value]
    product_info = dict(zip(table_key, table_value))
    return product_info
