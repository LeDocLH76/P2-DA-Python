class Book:
    def __init__(
            self,
            book_page_url,
            book_upc,
            book_title,
            book_price_inc_tax,
            book_price_excl_tax,
            book_available,
            book_description,
            book_category,
            book_rating,
            book_image_link
    ) -> None:
        self.book_page_url = book_page_url
        self.book_upc = book_upc
        self.book_title = book_title
        self.book_price_inc_tax = book_price_inc_tax
        self.book_price_excl_tax = book_price_excl_tax
        self.book_available = book_available
        self.book_description = book_description
        self.book_category = book_category
        self.book_rating = book_rating
        self.book_image_link = book_image_link
