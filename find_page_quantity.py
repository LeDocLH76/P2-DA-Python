from find_book_quantity import find_book_quantity


def find_page_quantity(soup) -> int:
    """For a BeautifulSoup object of a html category first page in attr,
    return the number of pages in the category

    """

    category_books_quantity = find_book_quantity(soup)
    category_full_page_quantity = category_books_quantity // 20
    category_last_page_quantity = 0
    if category_books_quantity % 20 != 0:
        category_last_page_quantity = 1
    category_total_page_quantity = \
        category_full_page_quantity + category_last_page_quantity
    return category_total_page_quantity
