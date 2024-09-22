import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar  # Asegúrate de instalar tkcalendar


class EventScheduler:
    def __init__(self, root):
        self.root = root
        self.root.title("Scheduler")

        # Crear Frames
        self.frame_input = tk.Frame(root)
        self.frame_input.pack(pady=10)

        self.frame_list = tk.Frame(root)
        self.frame_list.pack(pady=10)

        # Etiquetas y campos de entrada
        self.label_date = tk.Label(self.frame_input, text="Fecha:")
        self.label_date.grid(row=0, column=0)

        self.date_picker = Calendar(self.frame_input)
        self.date_picker.grid(row=0, column=1)

        self.label_time = tk.Label(self.frame_input, text="Hora:")
        self.label_time.grid(row=1, column=0)

        self.entry_time = tk.Entry(self.frame_input)
        self.entry_time.grid(row=1, column=1)

        self.label_desc = tk.Label(self.frame_input, text="Descripción:")
        self.label_desc.grid(row=2, column=0)

        self.entry_desc = tk.Entry(self.frame_input)
        self.entry_desc.grid(row=2, column=1)

        # Botones
        self.button_add = tk.Button(self.frame_input, text="Agregar Evento", command=self.add_event)
        self.button_add.grid(row=3, columnspan=2)

        self.button_delete = tk.Button(self.frame_input, text="Eliminar Evento Seleccionado", command=self.delete_event)
        self.button_delete.grid(row=4, columnspan=2)

        self.button_exit = tk.Button(self.frame_input, text="Salir", command=root.quit)
        self.button_exit.grid(row=5, columnspan=2)

        # TreeView para mostrar eventos
        self.tree = ttk.Treeview(self.frame_list, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()

    def add_event(self):
        date = self.date_picker.get_date()
        time = self.entry_time.get()
        desc = self.entry_desc.get()

        if date and time and desc:
            self.tree.insert("", "end", values=(date, time, desc))
            self.entry_time.delete(0, tk.END)
            self.entry_desc.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor completa todos los campos.")

    def delete_event(self):
        selected_item = self.tree.selection()
        if selected_item:
            confirm = messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar este evento?")
            if confirm:
                self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Advertencia", "Por favor selecciona un evento para eliminar.")


if __name__ == "__main__":
    root = tk.Tk()
    app = EventScheduler(root)
    root.mainloop()
