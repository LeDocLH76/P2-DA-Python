from constant import BASEURL
from library import Library
# from category import Category


library = Library(BASEURL)
# print(library.categories)
# print(library.categories_names)
for (link, name) in zip(library.categories, library.categories_names):
    print(f"La catégorie {name} est à l'adresse {link}")
# 	Category(url)
# category.name = Category(category)
# print(f"L'Url du site est: {library.site_url}")
# print(test_category.books_url)
