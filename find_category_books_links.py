from typing import List

from request_api import fetch_page
from make_the_soup import make_the_soup
from find_page_quantity import find_page_quantity
from find_page_books_links import find_page_books_links


def find_category_books_links(category_url: str) -> List[str]:
    """For a category link in attr,
    return a list of all the books links in the category
    """

    page_category_html = fetch_page(category_url)
    page_category_soup = make_the_soup(
        page_category_html.content, 'html.parser')
    # Find the number of 20 books's pages in the category
    category_total_page_quantity = find_page_quantity(page_category_soup)
    # Find the books links for the first page
    books_links = find_page_books_links(page_category_soup)
    # Find the books links for the other pages
    for page in range(category_total_page_quantity-1):
        page_offset = str(page + 2)
        # construct the end part of the next page url
        next_page = "page-" + page_offset + ".html"
        split_url = category_url.split("/")
        # Replace the end of the url
        split_url[-1] = next_page
        next_url = "/".join(split_url)
        page_category_html = fetch_page(next_url)
        next_page_category_soup = make_the_soup(
            page_category_html.content, 'html.parser')
        books_links_to_add = find_page_books_links(next_page_category_soup)
        books_links.extend(books_links_to_add)
    return books_links
