from constant import BASEURL
from library import Library
from category import Category


library = Library(BASEURL)
# print(library.categories_links)
# print(library.categories_names)
# for (link, name) in zip(library.categories_links, library.categories_names):
#     print(f"La catégorie {name} est à l'adresse {link}")
# print(library.categories_names[0])
# print(library.categories_links[0])
categories_names = library.categories_names

for index in range(len(categories_names)):
    categories_names[index] = Category(
        library.categories_links[index])
    print(categories_names[index].name + " " +
          categories_names[index].category_url)
    # print(categories_names[index].books_url)
