import tkinter as tk
from tkinter import messagebox


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")

        # Crear variables
        self.tasks = []

        # Crear la interfaz gráfica
        self.create_widgets()
        self.bind_shortcuts()

    def create_widgets(self):
        # Marco superior
        frame_top = tk.Frame(self.root)
        frame_top.pack(pady=10)

        # Campo de entrada para agregar nuevas tareas
        self.entry_task = tk.Entry(frame_top, width=35)
        self.entry_task.pack(side=tk.LEFT, padx=10)

        # Botón para añadir tareas
        btn_add_task = tk.Button(frame_top, text="Añadir Tarea", command=self.add_task)
        btn_add_task.pack(side=tk.LEFT)

        # Marco para la lista de tareas
        frame_list = tk.Frame(self.root)
        frame_list.pack(pady=10)

        # Lista para mostrar las tareas
        self.task_listbox = tk.Listbox(frame_list, height=10, width=50, selectmode=tk.SINGLE)
        self.task_listbox.pack(side=tk.LEFT)

        # Barra de desplazamiento para la lista de tareas
        scrollbar = tk.Scrollbar(frame_list)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)

        # Marco inferior con botones
        frame_bottom = tk.Frame(self.root)
        frame_bottom.pack(pady=10)

        # Botón para marcar como completada
        btn_mark_complete = tk.Button(frame_bottom, text="Marcar Completada", command=self.mark_completed)
        btn_mark_complete.grid(row=0, column=0, padx=10)

        # Botón para eliminar tarea
        btn_delete_task = tk.Button(frame_bottom, text="Eliminar Tarea", command=self.delete_task)
        btn_delete_task.grid(row=0, column=1, padx=10)

    def bind_shortcuts(self):
        # Asignar atajos de teclado
        self.root.bind('<Return>', lambda event: self.add_task())
        self.root.bind('<c>', lambda event: self.mark_completed())
        self.root.bind('<d>', lambda event: self.delete_task())
        self.root.bind('<Delete>', lambda event: self.delete_task())
        self.root.bind('<Escape>', lambda event: self.root.quit())

    def add_task(self):
        task = self.entry_task.get().strip()
        if task:
            self.tasks.append({'task': task, 'completed': False})
            self.entry_task.delete(0, tk.END)
            self.update_task_listbox()
        else:
            messagebox.showwarning("Entrada vacía", "Por favor, introduce una tarea.")

    def mark_completed(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index]['completed'] = not self.tasks[index]['completed']
            self.update_task_listbox()
        else:
            messagebox.showwarning("Sin selección", "Selecciona una tarea para marcar como completada.")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            self.update_task_listbox()
        else:
            messagebox.showwarning("Sin selección", "Selecciona una tarea para eliminar.")

    def update_task_listbox(self):
        # Limpiar la lista
        self.task_listbox.delete(0, tk.END)
        # Agregar tareas actualizadas a la lista
        for task in self.tasks:
            display_text = task['task']
            if task['completed']:
                display_text += " (Completada)"
            self.task_listbox.insert(tk.END, display_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
