import json
import csv

def json_to_csv(json_file, csv_file):
    # Read the JSON data
    with open(json_file, 'r') as f:
        tasks = json.load(f)  # Assumes the JSON file contains a list of tasks

    # Define the CSV column headers
    headers = ["ID", "Task Name", "Completed Status", "Priority"]

    # Write the data to the CSV file
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)  # Write the header row

        # Write each task as a row in the CSV
        for task in tasks:
            row = [
                task.get("id"),  # ID
                task.get("task_name"),  # Task Name
                task.get("completed"),  # Completed Status
                task.get("priority")  # Priority
            ]
            writer.writerow(row)

# Example usage
json_to_csv('tasks.json', 'tasks.csv')
