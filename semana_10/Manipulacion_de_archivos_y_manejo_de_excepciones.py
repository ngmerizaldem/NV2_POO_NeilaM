import os

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = self.cargar_inventario()

    def cargar_inventario(self):
        """Carga el inventario desde un archivo de texto."""
        productos = {}
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, 'r') as file:
                    for linea in file:
                        nombre, cantidad = linea.strip().split(',')
                        productos[nombre] = int(cantidad)
            except FileNotFoundError:
                print(f"Archivo {self.archivo} no encontrado, iniciando un nuevo inventario.")
            except PermissionError:
                print(f"Permiso denegado para leer el archivo {self.archivo}.")
            except Exception as e:
                print(f"Error inesperado al leer el archivo: {e}")
        return productos

    def guardar_inventario(self):
        """Guarda el inventario en un archivo de texto."""
        try:
            with open(self.archivo, 'w') as file:
                for nombre, cantidad in self.productos.items():
                    file.write(f"{nombre},{cantidad}\n")
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print(f"Permiso denegado para escribir en el archivo {self.archivo}.")
        except Exception as e:
            print(f"Error inesperado al escribir en el archivo: {e}")

    def agregar_producto(self, nombre, cantidad):
        """Agrega un producto al inventario."""
        if nombre in self.productos:
            self.productos[nombre] += cantidad
        else:
            self.productos[nombre] = cantidad
        self.guardar_inventario()

    def eliminar_producto(self, nombre):
        """Elimina un producto del inventario."""
        if nombre in self.productos:
            del self.productos[nombre]
            self.guardar_inventario()
        else:
            print(f"El producto {nombre} no existe en el inventario.")

    def actualizar_producto(self, nombre, cantidad):
        """Actualiza la cantidad de un producto existente en el inventario."""
        if nombre in self.productos:
            self.productos[nombre] = cantidad
            self.guardar_inventario()
        else:
            print(f"El producto {nombre} no existe en el inventario.")

    def mostrar_inventario(self):
        """Muestra el contenido del inventario."""
        if self.productos:
            for nombre, cantidad in self.productos.items():
                print(f"{nombre}: {cantidad}")
        else:
            print("El inventario está vacío.")

            def interfaz_usuario():
                inventario = Inventario()

                while True:
                    print("\nOpciones:")
                    print("1. Mostrar Inventario")
                    print("2. Agregar Producto")
                    print("3. Actualizar Producto")
                    print("4. Eliminar Producto")
                    print("5. Salir")
                    opcion = input("Seleccione una opción: ")

                    if opcion == '1':
                        inventario.mostrar_inventario()
                    elif opcion == '2':
                        nombre = input("Nombre del producto: ")
                        cantidad = int(input("Cantidad: "))
                        inventario.agregar_producto(nombre, cantidad)
                        print(f"Producto {nombre} añadido exitosamente.")
                    elif opcion == '3':
                        nombre = input("Nombre del producto: ")
                        cantidad = int(input("Nueva cantidad: "))
                        inventario.actualizar_producto(nombre, cantidad)
                        print(f"Producto {nombre} actualizado exitosamente.")
                    elif opcion == '4':
                        nombre = input("Nombre del producto: ")
                        inventario.eliminar_producto(nombre)
                        print(f"Producto {nombre} eliminado exitosamente.")
                    elif opcion == '5':
                        break
                    else:
                        print("Opción no válida. Intente de nuevo.")