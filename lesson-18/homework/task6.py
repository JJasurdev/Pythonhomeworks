# Load the employee dataset
df_employee = pd.read_csv('employee.csv')

# Normalize the salaries within each department
df_employee['Normalized_Salary'] = df_employee.groupby('Department')['Salary'].transform(
    lambda x: (x - x.mean()) / x.std()  # Normalizing the salary using Z-score
)

# Display the result
print("\nEmployee dataset with normalized salaries:")
print(df_employee[['Department', 'Salary', 'Normalized_Salary']].head())
