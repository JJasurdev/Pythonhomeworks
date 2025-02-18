import os

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"


class EmployeeManager:
    FILE = "employees.txt"

    def __init__(self):
        if not os.path.exists(self.FILE):
            open(self.FILE, 'w').close()

    def add_employee(self):
        emp_id = input("Enter Employee ID: ")
        if self._is_duplicate(emp_id):
            print("Employee ID already exists.")
            return
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        with open(self.FILE, 'a') as file:
            file.write(f"{emp_id},{name},{position},{salary}\n")
        print("Employee added successfully!")

    def view_all_employees(self):
        with open(self.FILE, 'r') as file:
            records = file.readlines()
            if not records:
                print("No records found.")
                return
            for record in records:
                print(record.strip())

    def search_employee(self):
        emp_id = input("Enter Employee ID to search: ")
        with open(self.FILE, 'r') as file:
            for line in file:
                if line.startswith(emp_id + ','):
                    print("Employee Found:\n" + line.strip())
                    return
            print("Employee not found.")

    def update_employee(self):
        emp_id = input("Enter Employee ID to update: ")
        records = []
        updated = False
        with open(self.FILE, 'r') as file:
            records = file.readlines()
        with open(self.FILE, 'w') as file:
            for line in records:
                if line.startswith(emp_id + ','):
                    name = input("Enter new name: ")
                    position = input("Enter new position: ")
                    salary = input("Enter new salary: ")
                    file.write(f"{emp_id},{name},{position},{salary}\n")
                    updated = True
                else:
                    file.write(line)
        print("Employee updated successfully!" if updated else "Employee not found.")

    def delete_employee(self):
        emp_id = input("Enter Employee ID to delete: ")
        records = []
        deleted = False
        with open(self.FILE, 'r') as file:
            records = file.readlines()
        with open(self.FILE, 'w') as file:
            for line in records:
                if not line.startswith(emp_id + ','):
                    file.write(line)
                else:
                    deleted = True
        print("Employee deleted successfully!" if deleted else "Employee not found.")

    def _is_duplicate(self, emp_id):
        with open(self.FILE, 'r') as file:
            for line in file:
                if line.startswith(emp_id + ','):
                    return True
        return False

    def menu(self):
        while True:
            print("\n1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_employee()
            elif choice == '2':
                self.view_all_employees()
            elif choice == '3':
                self.search_employee()
            elif choice == '4':
                self.update_employee()
            elif choice == '5':
                self.delete_employee()
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    manager = EmployeeManager()
    manager.menu()
