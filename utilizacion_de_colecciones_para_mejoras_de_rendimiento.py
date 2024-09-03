class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    def __repr__(self):
        return f"Libro(titulo='{self.titulo}', autor='{self.autor}', isbn='{self.isbn}')"

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __repr__(self):
        return f"Usuario(nombre='{self.nombre}', id_usuario={self.id_usuario})"

class Biblioteca:
    def __init__(self):
        self.libros = {}  # ISBN como clave, Libro como valor
        self.usuarios = set()  # Conjunto de IDs de usuarios

    def añadir_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Añadido: {libro}")
        else:
            print("El libro ya está en la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Eliminado libro con ISBN {isbn}.")
        else:
            print("El libro no está en la biblioteca.")

    def registrar_usuario(self, nombre, id_usuario):
        self.usuarios.add(id_usuario)
        print(f"Usuario registrado: {nombre} (ID {id_usuario})")

    def prestar_libro(self, isbn, id_usuario):
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros.pop(isbn)
            print(f"Prestado: {libro} a usuario ID {id_usuario}")
        else:
            print("No se puede realizar el préstamo.")

    def devolver_libro(self, libro):
        self.libros[libro.isbn] = libro
        print(f"Devuelto: {libro}")

# Ejemplo de uso
biblioteca = Biblioteca()

# Crear y añadir libros
libro1 = Libro("1984", "George Orwell", "978-0451524935")
libro2 = Libro("Brave New World", "Aldous Huxley", "978-0060850524")
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)

# Registrar usuarios
biblioteca.registrar_usuario("Juan Pérez", 1)
biblioteca.registrar_usuario("Ana López", 2)

# Prestar y devolver libros
biblioteca.prestar_libro("978-0451524935", 1)
biblioteca.devolver_libro(libro1)
