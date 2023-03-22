"""A l'attention du correcteur:
-Vu que le type de liste n'a pas était précisé au début du projet,
 mon choix intuitif était de choisir une liste bidirectionnelle,
 ainsi j'ai continué le projet avec ce type de données. Il est claire
 qu'une simple liste linéaire aurait pu résoudre le problème ou une liste circulaire en particulier pour bookLoanSolver.
 j'èspere que ce choix n'aurat pas de consequences négatives.
"""



class BookNode:
    """Attributs publiques, sans getter avec setter pour les modifier"""
    def __init__(self, titre, author, isbn, n, genre, next=None, previous=None):
        self.title = titre
        self.author = author
        self.isbn = isbn
        self.n = n
        self.type = genre
        self.next = next
        self.previous = previous

    def __str__(self):
        return f'{self.title}, {self.author}, {self.isbn}, {self.type}, {self.n}'

    def set_next(self, node):
        self.next = node

    def get_previous(self):
        return self.previous

    def set_previous(self, node):
        self.previous = node


class BookCatalog:
    def __init__(self):
        """List bidirectionnelle"""
        self.head = None
        self.count = 0

    def is_empty(self):
        return self.head is None

    def addBook(self, title, author, isbn, n, genre):
        """Adding it a the beginning of the list
        since it's more efficient in terms of time
        instead of searching for the last BookNode before adding the new one"""
        book = BookNode(title, author, isbn, n, genre)
        book.set_next(self.head)
        if self.head is not None:
            self.head.set_previous(book)
        self.head = book
        self.count += 1

    def removeBook(self, isbn):
        if not self.is_empty():
            act = self.head
            found = self.head.isbn == isbn
            while not found and act is not None:  # find the book with the same isbn
                act = act.next
                if act is not None:  # so we don't use .get_next() on the next elem to the last one which is None
                    found = True if act.isbn == isbn else False
            if found:  # if found do the work
                prev = act.previous
                if act.next is not None:  # if it's not the last node
                    act.next.set_previous(prev)  # set the link between the next and previous
                if prev is not None:  # if it's not the first
                    prev.set_next(act.next) # set the link with the next
                else:
                    self.head = act.next
                self.count -= 1

    def searchBook(self, query):
        if self.head is not None:
            current = self.head
            found = query in [current.title, current.author]
            while current is not None and not found:
                if query in [current.title, current.author]:
                    found = True
                else:
                    current = current.next
            if found:
                return current.itle, current.author, current.isbn, current.n

    @staticmethod
    def searchBook_by_type(self, genre, history, recommendations):
        """Etant donné un catalogue, un genre, une historique de lecyure et une liste de recommendations,
        Cette fonction rajoute aux recommendations tous les livres du meme type, non lue ou deja recommendés.
        Utilisation un set est envisageable : optimisation en terme de temps lors de la recherche d'un livre dans la liste de recommendations
        mais pas utilisé vu la specification du type de donnés a manipuler dans ce projet"""
        if self.head is not None:
            current = self.head  # Commencer par le 1er noeud de la liste chainée
            while current is not None:  # Pour iterer sur tous les Noeuds jusqu'au dernier
                if genre == current.type and current.title not in history + recommendations:  # livre ni lu ni recommendé et du meme type
                    recommendations.append(current.title)
                else:
                    current = current.next



