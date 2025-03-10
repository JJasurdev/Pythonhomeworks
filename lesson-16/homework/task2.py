import pandas as pd

# 1. Using the DataFrame from iris.json:
df_iris = pd.read_json('iris.json')

# Rename the columns to lowercase
df_iris.columns = df_iris.columns.str.lower()

# Select only the sepal_length and sepal_width columns
df_iris_selected = df_iris[['sepal_length', 'sepal_width']]
print("Iris dataset with selected columns:")
print(df_iris_selected.head())

# 2. From the titanic.xlsx DataFrame:
df_titanic = pd.read_excel('titanic.xlsx')

# Filter rows where the age of passengers is above 30
df_titanic_above_30 = df_titanic[df_titanic['age'] > 30]

# Count the number of male and female passengers
gender_count = df_titanic['sex'].value_counts()
print("\nCount of male and female passengers:")
print(gender_count)

# 3. From the Flights parquet file:
df_flights = pd.read_parquet('Flights.parquet')

# Extract and print only the origin, dest, and carrier columns
df_flights_selected = df_flights[['origin', 'dest', 'carrier']]
print("\nSelected columns from Flights dataset:")
print(df_flights_selected.head())

# Find the number of unique destinations
unique_destinations = df_flights['dest'].nunique()
print("\nNumber of unique destinations:", unique_destinations)

# 4. From the movie.csv file:
df_movie = pd.read_csv('movie.csv')

# Filter rows where duration is greater than 120 minutes
df_movie_filtered = df_movie[df_movie['duration'] > 120]

# Sort the filtered DataFrame by director_facebook_likes in descending order
df_movie_sorted = df_movie_filtered.sort_values(by='director_facebook_likes', ascending=False)
print("\nSorted movie dataset by director_facebook_likes:")
print(df_movie_sorted.head())
