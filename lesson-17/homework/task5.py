# Load the titanic dataset
df_titanic = pd.read_excel('titanic.xlsx')

# Define the function to classify passengers as Child or Adult
def classify_age_group(age):
    if age < 18:
        return 'Child'
    else:
        return 'Adult'

# Apply the function to create a new Age_Group column
df_titanic['Age_Group'] = df_titanic['age'].apply(classify_age_group)

# Display the result
print("Titanic dataset with Age_Group classification:")
print(df_titanic[['age', 'Age_Group']].head())

