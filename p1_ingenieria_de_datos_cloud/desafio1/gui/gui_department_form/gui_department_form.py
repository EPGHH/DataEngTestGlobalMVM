from tkinter import messagebox
import tkinter as tk

class GuiDepartmentForm:
    def __init__(self, root, departament_add):
        self.__departament_add = departament_add
        self.root = root
        self.root.title("Department Form")

        # Crear etiqueta y campo de entrada para el ID del departamento
        self.label_id = tk.Label(root, text="Department ID:")
        self.label_id.grid(row=0, column=0, padx=10, pady=5)
        self.entry_id = tk.Entry(root)
        self.entry_id.grid(row=0, column=1, padx=10, pady=5)

        # Crear etiqueta y campo de entrada para el nombre del departamento
        self.label_name = tk.Label(root, text="Department Name:")
        self.label_name.grid(row=1, column=0, padx=10, pady=5)
        self.entry_name = tk.Entry(root)
        self.entry_name.grid(row=1, column=1, padx=10, pady=5)

        # Botón para enviar la información del departamento
        self.submit_button = tk.Button(root, text="Submit", command=self.submit_department)
        self.submit_button.grid(row=2, column=0, columnspan=1, pady=10)

        # Botón para enviar la 
        self.close_button = tk.Button(root, text="Close", command=self.close_window)
        self.close_button.grid(row=2, column=1, columnspan=2, pady=10)

    def submit_department(self):
        # Obtener los valores ingresados por el usuario
        departament_id = self.entry_id.get()
        departament_name = self.entry_name.get()
        # Validar que se hayan ingresado valores en ambos campos
        if not departament_id or not departament_name:
            messagebox.showerror("Error", "Please enter both Department ID and Department Name.")
            return

        # Aquí puedes llamar a tu método _create_departament con los valores ingresados
        code = self.__departament_add._create_department(departament_id, departament_name)
        #print(code)
        # departament_adder._create_departament(departament_id, departament_name)
        # Mostrar un mensaje de éxito o error
        if code[0] == Warning:
            messagebox.showwarning(code[0], code[1])
        else:
            messagebox.showinfo(code[0], code[1])

    def close_window(self):
        self.root.destroy()