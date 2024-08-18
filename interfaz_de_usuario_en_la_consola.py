from clase_inventario import Inventario


def mostrar_menu():
    print("\n--- Menú de Gestión de Inventarios ---")
    print("1. Añadir producto")
    print("2. Eliminar producto por ID")
    print("3. Actualizar producto por ID")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")

def obtener_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opción (1-6): "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Error: Seleccione una opción válida (1-6).")
        except ValueError:
            print("Error: Ingrese un número entero válido.")

def solicitar_dato(tipo_dato, mensaje, obligatorio=True):
    while True:
        entrada = input(mensaje)
        if not entrada and not obligatorio:
            return None
        try:
            if tipo_dato == int:
                return int(entrada)
            elif tipo_dato == float:
                return float(entrada)
            elif tipo_dato == str:
                return entrada
        except ValueError:
            print(f"Error: Ingrese un valor válido para {tipo_dato.__name__}.")

def menu():
    inventario =Inventario()

    while True:
        mostrar_menu()
        opcion = obtener_opcion()

        if opcion == 1:
            id_producto = solicitar_dato(str, "Ingrese el ID del producto: ")
            nombre = solicitar_dato(str, "Ingrese el nombre del producto: ")
            cantidad = solicitar_dato(int, "Ingrese la cantidad del producto: ")
            precio = solicitar_dato(float, "Ingrese el precio del producto: ")
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == 2:
            id_producto = solicitar_dato(str, "Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == 3:
            id_producto = solicitar_dato(str, "Ingrese el ID del producto a actualizar: ")
            nueva_cantidad = solicitar_dato(int, "Ingrese la nueva cantidad (o presione Enter para omitir): ", obligatorio=False)
            nuevo_precio = solicitar_dato(float, "Ingrese el nuevo precio (o presione Enter para omitir): ", obligatorio=False)
            inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

        elif opcion == 4:
            nombre = solicitar_dato(str, "Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif opcion == 5:
            inventario.mostrar_todos_los_productos()

        elif opcion == 6:
            print("Saliendo del sistema de gestión de inventarios.")
            break

# Ejecutar el menú
menu()