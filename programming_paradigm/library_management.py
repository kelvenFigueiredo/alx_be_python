class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # atributo privado

    def check_out(self):
        """Marca o livro como emprestado."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marca o livro como disponível."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Retorna True se o livro estiver disponível para empréstimo."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # lista privada de livros

    def add_book(self, book):
        """Adiciona um livro ao acervo da biblioteca."""
        self._books.append(book)

    def check_out_book(self, title):
        """Procura o livro pelo título e tenta fazer o empréstimo."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        print(f"Book '{title}' is not available for checkout.")
        return False

    def return_book(self, title):
        """Procura o livro pelo título e tenta devolvê-lo."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        print(f"Book '{title}' was not checked out or doesn't exist.")
        return False

    def list_available_books(self):
        """Lista todos os livros disponíveis para empréstimo."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books available.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")