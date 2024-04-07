from departament_add.departament_add import DepartmentAdd
from job_position_add.job_position_add import JobPositionAdd
from gui.gui_department_form.gui_department_form import GuiDepartmentForm
from gui.gui_job_position_form.gui_job_position_form import GuiJobPositionForm
import tkinter as tk

# Crear la ventana principal de la aplicación
departament_add = DepartmentAdd()
root = tk.Tk()
app = GuiDepartmentForm(root, departament_add)
root.mainloop()

# Crear la ventana principal de la aplicación
job_position_add = JobPositionAdd()
root = tk.Tk()
app = GuiJobPositionForm(root, job_position_add)
root.mainloop()