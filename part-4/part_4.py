# Step 1 - Input function

# Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here

# 1 Input Statement
# title = input("Enter a book title:")
# print("The book name is " + title)

# 2 Input Statement
# author = input("Enter the books author:")
# print("The books author is " + author)

# 3 Input Statement
# year = input("Enter a book publication year:")
# print("The book was published in " + year)

# 4 Input Statement
# rating = input("Enter a book rating (1 to 5 float):")
# print("The books rating is " + rating)

# 5 Input Statement
# pages = input("Enter the total number of pages of the book:")
# print("The book has " + pages + " pages")


# Step 2 - Type conversion

# Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here

# title = input("Enter a book title:")
# author = input("Enter the books author:")
# year = int(input("Enter a book publication year:"))
# rating = float(input("Enter a book rating (1 to 5):"))
# pages = int(input("Enter the total number of pages of the book:"))


# Step 3 - Error handling

# Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here

# title = input("Enter a book title:")
# author = input("Enter the books author:")
# try:
#     year = int(input("Enter a book publication year:"))
# except:
#     year = int(input("Please enter a four digit number:"))
# try:
#     rating = float(input("Enter a book rating (1 to 5):"))
# except:
#     rating = float(input("Please choose a number between 1 and 5:"))
# try:
#     pages = int(input("Enter the total number of pages of the book:"))
# except:
#     pages = int(input("Please use a number:"))


# Step 4 - if/elif/else

# Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here

# def main_menu(book_choice):

#     options = input(
#         "Please type 'add-book' to add a new book, type 'see-books' to see all books, and type 'logout' to leave, once you've made your choice press enter: ")

#     if options == 'add-book':
#         book_choice.append(add_new_book())
#     elif options == "see-books":
#         display_books(book_choice)
#     elif options == "logout":
#         print("\n You've logged out")
#     else:
#         print("\n Please clearly type one of the three options")

# Step 5 - while loops

# Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

list_of_books = [
    {
        "title": "A Desolation Called Peace",
        "author": "Arkady Martine",
        "year": 2021,
        "rating": 4.6,
        "pages": 496
    },
    {
        "title": "Sea of Tranquility",
        "author": "Emily St. John Mandel",
        "year": 2022,
        "rating": 4.3,
        "pages": 255
    },
    {
        "title": "Eyes of the Void",
        "author": "Adrian Tchaikovsky",
        "year": 2022,
        "rating": 4.4,
        "pages": 551
    },
    {
        "title": "How High We Go in the Dark",
        "author": "Sequoia Nagamatsu",
        "year": 2022,
        "rating": 3.9,
        "pages": 290
    }
]


def add_new_book():
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

    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

    return book_dictionary


def print_all(list_of_books):

    print("\nHere's your book list...\n")

    for book in list_of_books:
        title = book["title"]
        author = book["author"]
        year = book["year"]
        rating = book["rating"]
        pages = book["pages"]

        print(
            f"Title: {title}, Author: {author}, Year: {year}, Rating: {rating}, Pages: {pages}")


def main_menu(books_source):

    active = True

    while active:
        choice = input("\nPlease type 'add' to add a book...\nPlease type 'see' to see all your books...\nPlease type 'total' to see the number of books in your library...\nPlease type 'pages' to see the total count of the pages of all your books...\nPlease type 'q' to log out.\nType here: ")

        if choice == "add":
            books_source.append(add_new_book())
        elif choice == "see":
            print_all(books_source)
        elif choice == "total":
            print(f"\nYou have a total of {len(books_source)} books.\n")
        elif choice == "pages":
            print(
                f"\nAll your books have {sum([x['pages'] for x in books_source])} pages in total!\n")
        elif choice == "q":
            print("\nYou are logged out")
            active = False
        else:
            print("\nOops! Please make sure your option is typed correctly.\n")


main_menu(list_of_books)
