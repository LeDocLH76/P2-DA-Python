from bs4 import BeautifulSoup
from constant import RATINGVALUES


def find_book_rating(page_book_soup: BeautifulSoup) -> int:
    """For a BeautifulSoup object of a html book page in attr,
    return the rating of the book

    """

    rating = page_book_soup.select_one(".star-rating")['class']
    rating = RATINGVALUES[rating[1]]
    return rating
