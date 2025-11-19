#books by author
author = Author.objects.get(name="george Orwell")
author_books = Book.objects.filter(author=author)

#list books in library 
library = Library.objects.get(name="Buruburu Library")
library_books = library.books.all()

for book in library_books:
    print(f"{book.title} by {book.author}, published on {book.published_date}")

#retrieve librarian
library =  Library.objects.get(name="Buruburu Library")
librarian = library.librarian