import csv

# Step 1: Read data from grades.csv and store it in a list of dictionaries
def read_grades(file_name):
    grades = []
    with open(file_name, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            grades.append(row)
    return grades

# Step 2: Calculate the average grade for each subject
def calculate_average_grades(grades):
    subject_grades = {}
    for entry in grades:
        subject = entry['Subject']
        grade = int(entry['Grade'])
        
        if subject in subject_grades:
            subject_grades[subject].append(grade)
        else:
            subject_grades[subject] = [grade]
    
    # Calculate the average for each subject
    average_grades = {}
    for subject, grades_list in subject_grades.items():
        average_grades[subject] = sum(grades_list) / len(grades_list)
    
    return average_grades

# Step 3: Write the average grades to a new CSV file
def write_average_grades(file_name, average_grades):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Subject', 'Average Grade'])  # Write header
        for subject, average in average_grades.items():
            writer.writerow([subject, average])

# Main program
if __name__ == "__main__":
    # Step 1: Read grades from grades.csv
    grades = read_grades('grades.csv')
    
    # Step 2: Calculate average grades
    average_grades = calculate_average_grades(grades)
    
    # Step 3: Write average grades to average_grades.csv
    write_average_grades('average_grades.csv', average_grades)
    
    print("Average grades have been calculated and written to 'average_grades.csv'.")