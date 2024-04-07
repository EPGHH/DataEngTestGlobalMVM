from departament_add.departament_add import DepartmentAdd
from job_position_add.job_position_add import JobPositionAdd
from employee_add.employee_add import EmployeeAdd
from gui.gui_department_form.gui_department_form import GuiDepartmentForm
from gui.gui_job_position_form.gui_job_position_form import GuiJobPositionForm
from gui.gui_employee_form.gui_employee_form import GuiEmployeeForm
import tkinter as tk

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Ventana Principal")

        # Botón para abrir la ventana para añadir departamento
        self.btn_open_department = tk.Button(master, text="Añadir Departamento", command=self.open_department)
        self.btn_open_department.pack(pady=10)

        # Botón para abrir la ventana para añadir posición de trabajo
        self.btn_open_job_position = tk.Button(master, text="Añadir Posición de Trabajo", command=self.open_job_position)
        self.btn_open_job_position.pack(pady=10)

        # Botón para abrir la ventana para añadir empleado
        self.btn_open_employee = tk.Button(master, text="Añadir Empleado", command=self.open_employee)
        self.btn_open_employee.pack(pady=10)

    def open_department(self):
        departament_add = DepartmentAdd()
        root_department = tk.Toplevel(self.master)
        app_department = GuiDepartmentForm(root_department, departament_add)

    def open_job_position(self):
        job_position_add = JobPositionAdd()
        root_job_position = tk.Toplevel(self.master)
        app_job_position = GuiJobPositionForm(root_job_position, job_position_add)

    def open_employee(self):
        employee_add = EmployeeAdd()
        root_employee = tk.Toplevel(self.master)
        app_employee = GuiEmployeeForm(root_employee, employee_add)

def main():
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()