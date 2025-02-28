import json
import csv

def load_tasks(filename="tasks.json"):
    """Load tasks from a JSON file."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename="tasks.json"):
    """Save tasks to a JSON file."""
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    """Display all tasks in a readable format."""
    print("\nTasks:")
    print("ID | Task Name       | Completed | Priority")
    print("---|----------------|-----------|---------")
    for task in tasks:
        print(f"{task['id']:2} | {task['task']:14} | {task['completed']} | {task['priority']}")

def calculate_stats(tasks):
    """Calculate and display task completion statistics."""
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task["completed"])
    pending_tasks = total_tasks - completed_tasks
    avg_priority = sum(task["priority"] for task in tasks) / total_tasks if total_tasks else 0
    
    print("\nTask Statistics:")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {avg_priority:.2f}")

def convert_json_to_csv(json_filename="tasks.json", csv_filename="tasks.csv"):
    """Convert tasks from JSON to CSV."""
    tasks = load_tasks(json_filename)
    with open(csv_filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Completed", "Priority"])
        for task in tasks:
            writer.writerow([task["id"], task["task"], task["completed"], task["priority"]])
    print(f"\nTasks have been successfully converted to {csv_filename}.")

if __name__ == "__main__":
    tasks = load_tasks()
    display_tasks(tasks)
    calculate_stats(tasks)
    convert_json_to_csv()
    
    # Save the tasks back to JSON if modifications were made (optional)
    save_tasks(tasks)
