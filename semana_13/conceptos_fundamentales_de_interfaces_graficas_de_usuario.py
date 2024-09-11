import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Función para agregar un elemento a la tabla
def agregar_item():
    item = entry_item.get()
    if item:
        tree.insert("", tk.END, values=(item,))
        entry_item.delete(0, tk.END)  # Limpia el campo de texto
    else:
        messagebox.showwarning("Advertencia", "Debe ingresar un elemento.")

# Función para limpiar la tabla
def limpiar_tabla():
    for item in tree.get_children():
        tree.delete(item)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI con Tabla")

# Etiqueta de Instrucción
label_item = tk.Label(ventana, text="Ingrese un elemento:")
label_item.pack(pady=5)

# Campo de texto para ingresar el elemento
entry_item = tk.Entry(ventana, width=30)
entry_item.pack(pady=5)

# Botón para agregar el elemento a la tabla
btn_agregar = tk.Button(ventana, text="Agregar", command=agregar_item)
btn_agregar.pack(pady=5)

# Tabla para mostrar los elementos agregados
tree = ttk.Treeview(ventana, columns=("Elemento"), show="headings", height=10)
tree.heading("Elemento", text="Elemento")
tree.pack(pady=5)

# Botón para limpiar la tabla
btn_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_tabla)
btn_limpiar.pack(pady=5)

# Iniciar el bucle principal de la ventana
ventana.mainloop()
