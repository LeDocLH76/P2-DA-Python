from bs4 import BeautifulSoup


def find_page_quantity(page_category_soup: BeautifulSoup) -> int:
    """For a BeautifulSoup object of a html category first page in attr,
    return the number of pages in the category

    """

    category_books_quantity = int(page_category_soup.form.find("strong").text)
    category_full_page_quantity = category_books_quantity // 20
    category_last_page_quantity = 0
    if category_books_quantity % 20 != 0:
        category_last_page_quantity = 1
    category_total_page_quantity = \
        category_full_page_quantity + category_last_page_quantity
    return category_total_page_quantity
