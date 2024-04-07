from departament_add.departament_add import DepartmentAdd
from gui.gui_department_form.gui_department_form import GuiDepartmentForm
import tkinter as tk

# Crear la ventana principal de la aplicación
departament_add = DepartmentAdd()
root = tk.Tk()
app = GuiDepartmentForm(root, departament_add)
root.mainloop()