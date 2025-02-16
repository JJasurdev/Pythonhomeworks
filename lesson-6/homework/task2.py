def display_menu():
    print("\nEmployee Records Manager")
    print("1. Add new employee record")
    print("2. View all employee records")
    print("3. Search for an employee by Employee ID")
    print("4. Update an employee's information")
    print("5. Delete an employee record")
    print("6. Exit")

def add_employee():
    with open("employees.txt", "a") as file:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        file.write(f"{emp_id}, {name}, {position}, {salary}\n")
        print("Employee record added successfully.")

def view_employees():
    try:
        with open("employees.txt", "r") as file:
            records = file.readlines()
            if records:
                print("\nEmployee Records:")
                for record in records:
                    print(record.strip())
            else:
                print("No employee records found.")
    except FileNotFoundError:
        print("No records found. Please add an employee first.")

def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    try:
        with open("employees.txt", "r") as file:
            records = file.readlines()
            found = False
            for record in records:
                if record.startswith(emp_id):
                    print(f"Employee found: {record.strip()}")
                    found = True
                    break
            if not found:
                print("Employee ID not found.")
    except FileNotFoundError:
        print("No records found. Please add an employee first.")

def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    found = False
    try:
        with open("employees.txt", "r") as file:
            records = file.readlines()
        
        with open("employees.txt", "w") as file:
            for record in records:
                if record.startswith(emp_id):
                    found = True
                    name = input("Enter new Name: ")
                    position = input("Enter new Position: ")
                    salary = input("Enter new Salary: ")
                    file.write(f"{emp_id}, {name}, {position}, {salary}\n")
                    print("Employee record updated successfully.")
                else:
                    file.write(record)
            
            if not found:
                print("Employee ID not found.")
    except FileNotFoundError:
        print("No records found. Please add an employee first.")

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    found = False
    try:
        with open("employees.txt", "r") as file:
            records = file.readlines()
        
        with open("employees.txt", "w") as file:
            for record in records:
                if record.startswith(emp_id):
                    found = True
                    print(f"Employee {emp_id} deleted successfully.")
                else:
                    file.write(record)
            
            if not found:
                print("Employee ID not found.")
    except FileNotFoundError:
        print("No records found. Please add an employee first.")

def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
