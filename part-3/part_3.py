my_book = {
    "title": "A Desolation Called Peace",
    "author": "Arkady Martine",
    "year": 2021,
    "rating": 4.6,
    "pages": 496
}

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below

# Step: 1


def book_info():
    pass

# Step: 2


def book_info(my_book):
    pass

# Step: 3


def book_info(my_book):
    book_string = (
        f'The books name is {my_book["title"]}, written by {my_book["author"]}, published in {my_book["year"]}, with a total of {my_book["pages"]} pages and a rating of {my_book["rating"]}!')

    return book_string


print(book_info(my_book))

# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below
# function 1


def book_name(d):
    return d["title"]


def book_details(d):
    return d.get("author")


def book_year(d):
    return d["year"]


def book_rating(d):
    return d["rating"]


def book_pages(d):
    return d["pages"]


print(book_name(my_book))
print(book_details(my_book))
print(book_year(my_book))
print(book_rating(my_book))
print(book_pages(my_book))

# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

# Function 1 - Full list of the dictionary


def book_details(d):
    return d


print(book_details(my_book))

# Function 2 - Change a value


def book_year_update(d):
    x = d.keys()
    my_book["year"] = "2010"
    return d


print(book_year_update(my_book))


# Function 3 - Check if a Key exists


def book_year_confirm(d):
    if "year" in d:
        return (f'The books year is {my_book["year"]}')


print(book_year_confirm(my_book))
