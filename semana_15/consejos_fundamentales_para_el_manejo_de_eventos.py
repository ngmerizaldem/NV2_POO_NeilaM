import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar, END

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")

        self.tasks = []

        # Campo de entrada
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)
        self.task_entry.bind('<Return>', self.add_task)  # Evento para Enter

        # Botón para añadir tarea
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        # Botón para marcar como completada
        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack(pady=5)

        # Botón para eliminar tarea
        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Listbox para mostrar tareas
        self.task_listbox = Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)
        self.task_listbox.bind('<Double-1>', self.complete_task)  # Doble clic para completar

        # Scrollbar
        self.scrollbar = Scrollbar(root)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

    def add_task(self, event=None):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, END)
        else:
            messagebox.showwarning("Advertencia", "Escribe una tarea.")

    def complete_task(self, event=None):
        try:
            selected_index = self.task_listbox.curselection()[0]
            completed_task = self.tasks[selected_index]
            # Cambiar el estado visualmente
            self.tasks[selected_index] = f"{completed_task} (Completada)"
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, END)
        for task in self.tasks:
            self.task_listbox.insert(END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
