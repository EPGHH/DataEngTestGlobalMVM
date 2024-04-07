from tkinter import messagebox, ttk
import tkinter as tk
import csv

class GuiJobPositionForm:
    def __init__(self, root, job_position_add):
        self.__job_position_add = job_position_add
        self.root = root
        self.root.title("Job Position Form")

        # Crear desplegable para mostrar la lista de nombres de departamentos
        self.label_dropdown = tk.Label(root, text="Select Department Name:")
        self.label_dropdown.grid(row=0, column=0, padx=10, pady=5)
        self.dropdown_var = tk.StringVar(root)
        self.dropdown = ttk.Combobox(root, textvariable=self.dropdown_var, state="readonly")
        self.dropdown.grid(row=0, column=1, padx=10, pady=5)
        self.load_departments()

        # Crear etiqueta y campo de entrada para el ID de la posicion de trabajo
        self.label_id = tk.Label(root, text="Job Position ID:")
        self.label_id.grid(row=1, column=0, padx=10, pady=5)
        self.entry_id = tk.Entry(root)
        self.entry_id.grid(row=1, column=1, padx=10, pady=5)

        # Crear etiqueta y campo de entrada para el nombre de la posicion de trabajo
        self.label_name = tk.Label(root, text="Job Position Name:")
        self.label_name.grid(row=2, column=0, padx=10, pady=5)
        self.entry_name = tk.Entry(root)
        self.entry_name.grid(row=2, column=1, padx=10, pady=5)

        # Botón para enviar la información de la posicion de trabajo
        self.submit_button = tk.Button(root, text="Submit", command=self.submit_job_position)
        self.submit_button.grid(row=3, column=0, columnspan=1, pady=10)

        # Botón para enviar la 
        self.close_button = tk.Button(root, text="Close", command=self.close_window)
        self.close_button.grid(row=3, column=1, columnspan=2, pady=10)

    def load_departments(self):
        # Cargar los nombres de los departamentos desde el archivo CSV
        department_names = []
        with open('data_resources/department.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Omitir la primera fila (cabecera)
            for row in reader:
                department_names.append(row[1])  # Se asume que el nombre del departamento está en la segunda columna
        self.dropdown['values'] = department_names

    def get_department_id_by_name(self, department_name):
        # Obtener el ID del departamento dado su nombre
        with open('data_resources/department.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Omitir la primera fila (cabecera)
            for row in reader:
                if row[1] == department_name:
                    return row[0]  # Devolver el ID del departamento
        return None  # Si no se encuentra el nombre del departamento

    def submit_job_position(self):
        # Obtener los valores ingresados por el usuario
        department_name = self.dropdown_var.get()
        department_id = self.get_department_id_by_name(department_name)
        job_position_id = self.entry_id.get()
        job_position_name = self.entry_name.get()
        # Validar que se hayan ingresado valores en ambos campos
        if not job_position_id or not department_id or not job_position_name:
            messagebox.showerror("Error", "Please enter both Job Position ID and Job Position Name.")
            return

        # Aquí puedes llamar a tu método _create_departament con los valores ingresados
        code = self.__job_position_add._create_job_position(job_position_id, department_id, job_position_name)
        #print(code)
        # job_position_adder._create_departament(departament_id, departament_name)
        # Mostrar un mensaje de éxito o error
        if code[0] == Warning:
            messagebox.showwarning(code[0], code[1])
        else:
            messagebox.showinfo(code[0], code[1])

    def close_window(self):
        self.root.destroy()