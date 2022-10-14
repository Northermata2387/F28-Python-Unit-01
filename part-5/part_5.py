

# Step 1 - Store data in a .txt

# This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here

def add_new_book(book_source):
    title = input("\nEnter a book title:")
    author = input("Enter the books author:")
    try:
        year = int(input("Enter a book publication year:"))
    except:
        year = int(input("Please enter a four digit number:"))
    try:
        rating = float(input("Enter a book rating (1 to 5):"))
    except:
        rating = float(input("Please choose a number between 1 and 5:"))
    try:
        pages = int(input("Enter the total number of pages of the book:"))
    except:
        pages = int(input("Please use a number:"))

    with open(book_source, "a") as file:
        file.write(f"\n{title}, {author}, {year}, {rating}, {pages}")

# Step 2 - Read data from a .txt

# Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.


# Code here
# with open("books.txt", "a") as f:
#     f.write("\nA Desolation Called Peace, Arkady Martine, 2021, 4.6, 496")


# def view_books_original(book_source):

#     print("\nHere are all your books...\n")

#     with open(book_source, "r") as f:
#         file = f.readlines()

#         for line in file:
#             title, author, year, rating, pages = line.split(", ")

#             print(
#                 f"Title: {title}, Author: {author}, Year: {year}, Rating: {rating}, Pages: {pages}")


# view_books_original("books.txt")


# Step 3 - if __name__ == "__main__":

# Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script

# Step 4 - Expand and refactor

# Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!


def get_books_as_list_of_dictionaries(book_source):
    books_list = []
    with open(book_source, "r") as f:
        file = f.readlines()
        for line in file:
            title, author, year, rating, pages = line.split(", ")
            books_list.append({
                "title": title,
                "author": author,
                "year": int(year),
                "rating": float(rating),
                "pages": int(pages)
            })
    return books_list


def get_book_printed(book):
    print(
        f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Rating: {book['rating']}, Pages: {book['pages']}")


def view_books(book_source):
    print("\nHere are all your books...\n")
    for book in get_books_as_list_of_dictionaries(book_source):
        get_book_printed(book)


def get_highest_rated_book(book_source):
    list = get_books_as_list_of_dictionaries(book_source)
    return max(list, key=lambda x: int(x["rating"]))


def get_lowest_rated_book(book_source):
    list = get_books_as_list_of_dictionaries(book_source)
    return min(list, key=lambda x: int(x["rating"]))


def get_sorted_list_by_rating(book_source):
    print("\nSee all your books ordered by rating...\n")
    list = get_books_as_list_of_dictionaries(book_source)
    list = sorted(list, key=lambda x: int(x["rating"]), reverse=True)
    for book in list:
        get_book_printed(book)


def main_menu(book_source):

    active = True

    while active:
        choice = input("""
Please type 'add' to add a book...
Please type 'see' to see all your books...
Please type 'total' to see the number of books in your library...
Please type 'pages' to see the total number of pages of all books...
Please type 'best' to see the highest rated book in your library...
Please type 'worst' to see the lowest rated book in your library...
Please type 'rating' to see your books listed by rating...
Please type 'q' to log out.
Type here: """)

        if choice == "add":
            add_new_book(book_source)
        elif choice == "see":
            view_books(book_source)
        elif choice == "total":
            print(
                f"\nYou have a total of {len(get_books_as_list_of_dictionaries(book_source))} books.\n")
        elif choice == "pages":
            print(
                f"\nYour books page count totals {sum([x['pages'] for x in get_books_as_list_of_dictionaries(book_source)])} pages!\n")
        elif choice == "best":
            print("\nHere is the best book...\n")
            get_book_printed(get_highest_rated_book(book_source))
        elif choice == "worst":
            print("\nHere is the worst book...\n")
            get_book_printed(get_lowest_rated_book(book_source))
        elif choice == "rating":
            get_sorted_list_by_rating(book_source)
        elif choice == "q":
            print("\nYou are Logged out!")
            active = False
        else:
            print("\nOops! Please make sure your option is typed correctly.\n")


if __name__ == "__main__":
    main_menu("books.txt")
