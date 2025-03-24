import json

class BookCollection:
    """A class to manage collection of books, allowing users to store and organize their reading materials!!"""

    def __init__(self) -> None:
        """Initialize a new book collection with an empty list and set up file storage."""
        self.book_list = []
        self.storage_file = "books_data.json"
        self.read_from_file()

    def read_from_file(self):
        """Load saved books from a JSON file into memory.
        If the file doesn't exist or is corrupted, start with an empty collection."""
        try:
            with open(self.storage_file, "r") as file:
                self.book_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.book_list = []

    def save_to_file(self):
        """Save the current book collection to a JSON file."""
        with open(self.storage_file, "w") as file:
            json.dump(self.book_list, file, indent=4)

    def create_new_book(self):
        """Add a new book to the collection by gathering information from the user."""
        book_title = input("Enter book title: ")
        book_author = input("Enter author name: ")
        year_published = input("Enter publication year: ")
        book_genre = input("Enter genre: ")

        is_book_read = (
            input("Have you read this book? (yes/no): ").strip().lower() == "yes"
        )

        new_book = {
            "title": book_title,
            "author": book_author,
            "year": year_published,
            "genre": book_genre,  # Fixed typo here
            "read": is_book_read
        }

        self.book_list.append(new_book)
        self.save_to_file()
        print("Book added successfully!")

    def delete_book(self):
        """Remove the book from the collection using it's title."""
        book_title = input("Enter the title to remove the book:")
        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                self.book_list.remove(book)
                self.save_to_file()
                print("Book removed successfully")
                return
        print("Book not found'\n")

    def find_book(self):
        """Search for the books in the collection by title or author name."""
        search_type = input("Search by:\n1. Title\n2. Author\nEnter your choice: ")
        search_text = input("Enter search term: ").lower()
        found_books = [
            book
            for book in self.book_list
            if search_text in book ["title"].lower()
            or search_text in book ["author"].lower()
        ]

        if found_books:
            print("Matching books:")
            for index, book in enumerate(found_books, 1):
                reading_Status = "Read" if book["read"] else "Unread"
                print(f"{index}. {book["title"]} by {book["author"]} ({book["year"]}) - {book["genre"] - {reading_Status}}")
        else:
            print("No matching books found.\n")


    def start_application(self):
        """Run the main application loop with a user-friendly menu interface."""
        while True:
            print("Welcome! to your book collection manager 📗")
            print("1. Add a new book")
            print("2. Remove a book")
            print("3. Search for books")
            print("4. Update book details")
            print("5. View all books")
            print("6. View reading progress")
            print("7. Exit")

            user_choice = input("Please choose an option (1-7): ")

            if user_choice == "1":
                self.create_new_book()
            elif user_choice == "2":
                self.delete_book()
            elif user_choice == "3":
                self.find_book()
            elif user_choice == "7":
                print("Exiting the application. Goodbye!")
                break  # Exit the loop
            else:
                print("This option is not implemented yet. Please choose another option.")

if __name__ == "__main__":
    book_manager = BookCollection()
    book_manager.start_application()