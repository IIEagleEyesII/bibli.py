from partie1_catalogue_des_livres import BookCatalog, BookNode


class Patron:
    def __init__(self, username, book_types):
        self.username = username
        self.book_types = book_types
        self.book_history = []

    def add_to_history(self, new_book):
        self.book_history.append(new_book)

    def get_history_titles(self):
        res = []
        for book in self.book_history:
            #if book is not None:
            res.append(book.title)
        return res


def recommendBooks(client: Patron, bookCatalog: BookCatalog):
    """Extrait les genres préférés de l'utilisateur
    Utilise _recommendBooks pour iterer recursivement sur chaque genre"""
    recommendations = []
    client_types = client.book_types
    _recommend_book(client, bookCatalog, client_types, recommendations)
    return recommendations


def _recommend_book(client: Patron, bookCatalog: BookCatalog, client_types, recommendations):
    """Extrait l'historique de lecture de l'utilisateur,
    fait un appel recursif sur chaque genre,
    utilise la methode searchBook_by_type pour ajouter les livres du meme type,pas encore recommendés et
    non présent dans l'historique de lecture"""
    if len(client_types) != 0:
        history_by_titles = client.get_history_titles()  # Renvoie les titres des livres lues par le lecteur
        current_type = client_types[0]
        while BookCatalog.searchBook_by_type(self=bookCatalog, genre=current_type, recommendations=recommendations,
                                             history=history_by_titles):
            continue
        _recommend_book(client=client, bookCatalog=bookCatalog, client_types=client_types[1:],
                        recommendations=recommendations)

