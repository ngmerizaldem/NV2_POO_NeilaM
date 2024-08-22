class Inventario:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto):
        if not any(p.get_id() == producto.get_id() for p in self.productos):
            self.productos.append(producto)
            print("Producto añadido exitosamente.")
        else:
            print("Error: Ya existe un producto con el mismo ID.")

    def eliminar_producto(self, id_producto):
        producto_a_eliminar = None
        for producto in self.productos:
            if producto.get_id() == id_producto:
                producto_a_eliminar = producto
                break
        if producto_a_eliminar:
            self.productos.remove(producto_a_eliminar)
            print("Producto eliminado exitosamente.")
        else:
            print("Error: No se encontró un producto con el ID proporcionado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)
                print("Producto actualizado exitosamente.")
                return
        print("Error: No se encontró un producto con el ID proporcionado.")

    def buscar_producto_por_nombre(self, nombre):
        productos_encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if productos_encontrados:
            for producto in productos_encontrados:
                print(producto)
        else:
            print("No se encontraron productos con el nombre proporcionado.")

    def mostrar_todos_los_productos(self):
        if self.productos:
            for producto in self.productos:
                print(producto)
        else:
            print("No hay productos en el inventario.")