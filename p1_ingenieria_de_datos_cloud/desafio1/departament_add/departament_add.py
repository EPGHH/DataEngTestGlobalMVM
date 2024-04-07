import csv
import os

class DepartmentAdd:
    def __init__(self):
        pass

    def _create_department(self, department_id, department_name):
        # Check if department_id is a positive integer
        try:
            department_id = int(department_id)
            if department_id <= 0:
                return "Error", "Department ID must be a positive integer."
        except ValueError:
            return "Error", "Department ID must be a positive integer."

        # Check if the CSV file exists
        if os.path.exists('data_resources/department.csv'):
            # Check if the department_id already exists
            with open('data_resources/department.csv', 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and row[0] == str(department_id):
                        return "Warning", "Department ID already exists."

            # Open the CSV file in append mode and write department details
            with open('data_resources/department.csv', 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)

                # Write department details
                writer.writerow([department_id, department_name])
        elif not os.path.exists('data_resources'):
            # Create the 'data_resources' directory if it doesn't exist
            os.makedirs('data_resources')

            # Create the CSV file and write CSV header and department details
            with open('data_resources/department.csv', 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)

                # Write CSV header
                writer.writerow(['departament_id', 'departament_name'])

                # Write department details
                writer.writerow([department_id, department_name])
        else:
            # Create the CSV file and write CSV header and department details
            with open('data_resources/department.csv', 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)

                # Write CSV header
                writer.writerow(['departament_id', 'departament_name'])

                # Write department details
                writer.writerow([department_id, department_name])

        return "Success", "Department added successfully."
