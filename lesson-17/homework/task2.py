import pandas as pd

# Load the titanic dataset
df_titanic = pd.read_excel('titanic.xlsx')

# Group by Pclass and calculate the average age, total fare, and count of passengers
df_grouped_titanic = df_titanic.groupby('Pclass').agg(
    avg_age=('age', 'mean'),
    total_fare=('fare', 'sum'),
    passenger_count=('age', 'count')
).reset_index()

# Display the result
print("Grouped Aggregations on Titanic:")
print(df_grouped_titanic)
