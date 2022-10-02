from constant import BASEURL
from request_api import fetch_page
from make_the_soup import make_the_soup
from library import Library
from category import Category


site_url = f"{BASEURL}index.html"
page_main = fetch_page(site_url)
page_main_soup = make_the_soup(page_main.content, "html.parser")
library = Library(page_main_soup)

# print(library.get_categories_links)
# print(library.get_categories_names)

# for (link, name) in zip(library.get_categories_links,
#                         library.get_categories_names):
#     print(f"La catégorie {name} est à l'adresse {link}")

url_to_fetch = library.get_categories_links[3]

page_category = fetch_page(url_to_fetch)
page_category_soup = make_the_soup(page_category.content, "html.parser")
category = Category(page_category_soup)
print(f"Longueur de la liste = {len(category.get_books_links)}")

print(category.next_page)

while category.next_page is not None:
    next_page_url = url_to_fetch.split("/")[:-1]
    next_page_url.append(category.next_page)
    next_page_url = "/".join(next_page_url)
    print(f"Next page url = {next_page_url}")

    page_category = fetch_page(next_page_url)
    page_category_soup = make_the_soup(page_category.content, "html.parser")

    category.add_books_links(page_category_soup)
    print(category.next_page)
    print(f"Longueur de la liste = {len(category.get_books_links)}")

# categories_names = library.categories_names

# for index in range(len(categories_names)):
#     categories_names[index] = Category(
#         library.categories_links[index])
#     print(categories_names[index].name + " " +
#           categories_names[index].category_url)
#     # print(categories_names[index].books_url)
