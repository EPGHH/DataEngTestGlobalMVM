import csv
import os

class EmployeeAdd:
    def __init__(self):
        pass

    def _create_employee(self, employee_id, fk_job_position_id, employee_name, hire_date, 
                             salary, birth_date, phone_number, email, address):
        # Check if job_position_id is a positive integer
        try:
            employee_id = int(employee_id)
            if employee_id <= 0:
                return "Error", "employee_id must be a positive integer."
        except ValueError:
            return "Error", "employee_id must be a positive integer."
        
        # Check if fk_departament_id is a positive integer
        try:
            fk_job_position_id = int(fk_job_position_id)
            if fk_job_position_id <= 0:
                return "Error", "fk_job_position_id must be a positive integer."
        except ValueError:
            return "Error", "fk_job_position_id must be a positive integer."

        # Check if the CSV file exists
        if os.path.exists('data_resources/employee.csv'):
            # Check if the job_position_id and fk_departament_id pair already exists
            with open('data_resources/employee.csv', 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == str(employee_id):
                        return "Warning", "employee_id already exists."

            # Open the CSV file in append mode and write employee details
            with open('data_resources/employee.csv', 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)

                # Write employee details
                writer.writerow([employee_id, fk_job_position_id, employee_name, hire_date, 
                                    salary, birth_date, phone_number, email, address])
        elif not os.path.exists('data_resources'):
            # Create the 'data_resources' directory if it doesn't exist
            os.makedirs('data_resources')

            # Create the CSV file and write CSV header and employee details
            with open('data_resources/employee.csv', 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)

                # Write CSV header
                writer.writerow(["employee_id", "fk_job_position_id", "employee_name", "hire_date", 
                                 "salary", "birth_date", "phone_number", "email", "address"])

                # Write employee details
                writer.writerow([employee_id, fk_job_position_id, employee_name, hire_date, 
                                    salary, birth_date, phone_number, email, address])
        else:
            # Create the CSV file and write CSV header and employee details
            with open('data_resources/employee.csv', 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)

                # Write CSV header
                writer.writerow(["employee_id", "fk_job_position_id", "employee_name", "hire_date", 
                                 "salary", "birth_date", "phone_number", "email", "address"])

                # Write employee details
                writer.writerow([employee_id, fk_job_position_id, employee_name, hire_date, 
                                    salary, birth_date, phone_number, email, address])

        return "Success", "Employee added successfully."
