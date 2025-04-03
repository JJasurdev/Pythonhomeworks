import pandas as pd

# Load the Titanic dataset
df_titanic = pd.read_excel('titanic.xlsx')

# Create a pipeline for Titanic dataset
def filter_survived(df):
    return df[df['Survived'] == 1]

def fill_missing_age(df):
    df['Age'] = df['Age'].fillna(df['Age'].mean())
    return df

def create_fare_per_age(df):
    df['Fare_Per_Age'] = df['Fare'] / df['Age']
    return df

# Apply the pipeline using .pipe()
df_titanic_pipeline = (df_titanic
                       .pipe(filter_survived)
                       .pipe(fill_missing_age)
                       .pipe(create_fare_per_age))

# Display the result
print("Titanic dataset with pipeline transformations:")
print(df_titanic_pipeline[['Survived', 'Age', 'Fare', 'Fare_Per_Age']].head())
