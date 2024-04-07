import csv
import os

class JobPositionAdd:
    def __init__(self):
        pass

    def _create_job_position(self, job_position_id, fk_departament_id, job_position_name):
        # Check if job_position_id is a positive integer
        try:
            job_position_id = int(job_position_id)
            if job_position_id <= 0:
                return "Error", "Job position id must be a positive integer."
        except ValueError:
            return "Error", "Job position id must be a positive integer."
        
        # Check if fk_departament_id is a positive integer
        try:
            fk_departament_id = int(fk_departament_id)
            if fk_departament_id <= 0:
                return "Error", "fk_departament_id must be a positive integer."
        except ValueError:
            return "Error", "fk_departament_id must be a positive integer."

        # Check if the CSV file exists
        if os.path.exists('data_resources/job_position.csv'):
            # Check if the job_position_id and fk_departament_id pair already exists
            with open('data_resources/job_position.csv', 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == str(job_position_id):
                        return "Warning", "Job position ID already exists."

            # Open the CSV file in append mode and write job_position details
            with open('data_resources/job_position.csv', 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)

                # Write job_position details
                writer.writerow([job_position_id, fk_departament_id, job_position_name])
        elif not os.path.exists('data_resources'):
            # Create the 'data_resources' directory if it doesn't exist
            os.makedirs('data_resources')

            # Create the CSV file and write CSV header and job_position details
            with open('data_resources/job_position.csv', 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)

                # Write CSV header
                writer.writerow(["job_position_id", "fk_departament_id", "job_position_name"])

                # Write job_position details
                writer.writerow([job_position_id, fk_departament_id, job_position_name])
        else:
            # Create the CSV file and write CSV header and job_position details
            with open('data_resources/job_position.csv', 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)

                # Write CSV header
                writer.writerow(["job_position_id", "fk_departament_id", "job_position_name"])

                # Write job_position details
                writer.writerow([job_position_id, fk_departament_id, job_position_name])

        return "Success", "Job position added successfully."
