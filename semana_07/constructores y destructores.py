class Archivo:
    def __init__(self, nombre_archivo, modo):
        """
        Constructor de la clase Archivo.
        Abre el archivo con el nombre y modo especificado.

        :param nombre_archivo: Nombre del archivo a abrir
        :param modo: Modo en el que se abrirá el archivo (ej. 'r' para leer, 'w' para escribir)
        """
        self.nombre_archivo = nombre_archivo
        self.modo = modo
        self.archivo = None
        self.abrir_archivo()

    def abrir_archivo(self):
        """
        Método para abrir el archivo con el nombre y modo especificado.
        """
        try:
            self.archivo = open(self.nombre_archivo, self.modo)
            print(f"Archivo '{self.nombre_archivo}' abierto en modo '{self.modo}'.")
        except IOError as e:
            print(f"No se pudo abrir el archivo: {e}")

    def escribir(self, contenido):
        """
        Método para escribir contenido en el archivo si está abierto en modo escritura.

        :param contenido: Contenido a escribir en el archivo
        """
        if self.archivo and not self.archivo.closed:
            if 'w' in self.modo or 'a' in self.modo:
                self.archivo.write(contenido)
                print(f"Contenido escrito en '{self.nombre_archivo}'.")
            else:
                print("El archivo no está abierto en modo escritura.")
        else:
            print("El archivo no está abierto.")

    def leer(self):
        """
        Método para leer el contenido del archivo si está abierto en modo lectura.

        :return: Contenido del archivo
        """
        if self.archivo and not self.archivo.closed:
            if 'r' in self.modo:
                return self.archivo.read()
            else:
                print("El archivo no está abierto en modo lectura.")
        else:
            print("El archivo no está abierto.")

    def __del__(self):
        """
        Destructor de la clase Archivo.
        Cierra el archivo si está abierto.
        """
        if self.archivo and not self.archivo.closed:
            self.archivo.close()
            print(f"Archivo '{self.nombre_archivo}' cerrado.")