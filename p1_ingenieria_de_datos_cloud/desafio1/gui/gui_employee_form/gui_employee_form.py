from tkinter import messagebox, ttk
import tkinter as tk
import csv

class GuiEmployeeForm:
    def __init__(self, root, employee_add):
        self.__employee_add = employee_add
        self.root = root
        self.root.title("Employee Form")

        # Crear desplegable para mostrar la lista de nombres de Posiciones de trabajo
        self.label_dropdown = tk.Label(root, text="Select Job Position Name:")
        self.label_dropdown.grid(row=0, column=0, padx=10, pady=5)
        self.dropdown_var = tk.StringVar(root)
        self.dropdown = ttk.Combobox(root, textvariable=self.dropdown_var, state="readonly")
        self.dropdown.grid(row=0, column=1, padx=10, pady=5)
        self.load_job_positions()

        # Crear etiqueta y campo de entrada para el ID del empleado
        self.label_id = tk.Label(root, text="Job Employee ID:")
        self.label_id.grid(row=1, column=0, padx=10, pady=5)
        self.entry_id = tk.Entry(root)
        self.entry_id.grid(row=1, column=1, padx=10, pady=5)

        # Crear etiqueta y campo de entrada para el nombre del empleado
        self.label_name = tk.Label(root, text="Job Employee Name:")
        self.label_name.grid(row=2, column=0, padx=10, pady=5)
        self.entry_name = tk.Entry(root)
        self.entry_name.grid(row=2, column=1, padx=10, pady=5)

        # Crear etiqueta y campo de entrada para el Hire Date
        self.label_hire = tk.Label(root, text="Hire Date:")
        self.label_hire.grid(row=3, column=0, padx=10, pady=5)
        self.entry_hire = tk.Entry(root)
        self.entry_hire.grid(row=3, column=1, padx=10, pady=5)

        # Crear etiqueta y campo de entrada para el salary
        self.label_salary = tk.Label(root, text="salary:")
        self.label_salary.grid(row=4, column=0, padx=10, pady=5)
        self.entry_salary = tk.Entry(root)
        self.entry_salary.grid(row=4, column=1, padx=10, pady=5)

        # Crear etiqueta y campo de entrada para el Birth Date
        self.label_birth = tk.Label(root, text="Birth Date:")
        self.label_birth.grid(row=5, column=0, padx=10, pady=5)
        self.entry_birth = tk.Entry(root)
        self.entry_birth.grid(row=5, column=1, padx=10, pady=5)

        # Crear etiqueta y campo de entrada para el Phone Number
        self.label_phone = tk.Label(root, text="Phone Number:")
        self.label_phone.grid(row=6, column=0, padx=10, pady=5)
        self.entry_phone = tk.Entry(root)
        self.entry_phone.grid(row=6, column=1, padx=10, pady=5)

        # Crear etiqueta y campo de entrada para el Email
        self.label_email = tk.Label(root, text="Email:")
        self.label_email.grid(row=7, column=0, padx=10, pady=5)
        self.entry_email = tk.Entry(root)
        self.entry_email.grid(row=7, column=1, padx=10, pady=5)

        # Crear etiqueta y campo de entrada para el Address
        self.label_address = tk.Label(root, text="Address:")
        self.label_address.grid(row=8, column=0, padx=10, pady=5)
        self.entry_address = tk.Entry(root)
        self.entry_address.grid(row=8, column=1, padx=10, pady=5)


        # Botón para enviar la información de la posicion de trabajo
        self.submit_button = tk.Button(root, text="Submit", command=self.submit_employee)
        self.submit_button.grid(row=9, column=0, columnspan=1, pady=10)

        # Botón para enviar la 
        self.close_button = tk.Button(root, text="Close", command=self.close_window)
        self.close_button.grid(row=9, column=1, columnspan=2, pady=10)

    def load_job_positions(self):
        # Cargar los nombres de los departamentos desde el archivo CSV
        job_position_name = []
        with open('data_resources/job_position.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Omitir la primera fila (cabecera)
            for row in reader:
                job_position_name.append(row[2])  # Se asume que el nombre del departamento está en la segunda columna
        self.dropdown['values'] = job_position_name

    def get_job_position_id_by_name(self, job_position_name):
        # Obtener el ID del departamento dado su nombre
        with open('data_resources/job_position.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Omitir la primera fila (cabecera)
            for row in reader:
                if row[2] == job_position_name:
                    return row[0]  # Devolver el ID de la job position
        return None  # Si no se encuentra el nombre de la job position

    def submit_employee(self):
        # Obtener los valores ingresados por el usuario
        job_position_name = self.dropdown_var.get()
        job_position_id = self.get_job_position_id_by_name(job_position_name)
        employee_id = self.entry_id.get()
        employee_name = self.entry_name.get()
        hire_date = self.entry_hire.get()
        salary = self.entry_salary.get()
        birth_date = self.entry_birth.get()
        phone_number = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.entry_address.get()

        # Validar que se hayan ingresado valores en ambos campos
        if not employee_id or not job_position_id or not employee_name or not hire_date or not salary\
            or not birth_date or not phone_number:
            messagebox.showerror("Error", "Please enter both Job Position ID and Job Position Name.")
            return

        # Aquí puedes llamar a tu método _create_departament con los valores ingresados
        code = self.__employee_add._create_employee(employee_id, job_position_id, employee_name, hire_date, salary, 
                                                            birth_date, phone_number, email, address)
        #print(code)
        # job_position_adder._create_departament(departament_id, departament_name)
        # Mostrar un mensaje de éxito o error
        if code[0] == Warning:
            messagebox.showwarning(code[0], code[1])
        else:
            messagebox.showinfo(code[0], code[1])

    def close_window(self):
        self.root.destroy()