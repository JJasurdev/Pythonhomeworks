import pandas as pd

# 1. From iris.json: Calculate the mean, median, and standard deviation for each numerical column.
df_iris = pd.read_json('iris.json')

# Calculate the mean, median, and standard deviation for each numerical column
iris_statistics = df_iris.describe().T[['mean', '50%', 'std']]
iris_statistics.rename(columns={'50%': 'median'}, inplace=True)
print("Iris dataset statistics (mean, median, std):")
print(iris_statistics)

# 2. From titanic.xlsx: Find the minimum, maximum, and sum of passenger ages.
df_titanic = pd.read_excel('titanic.xlsx')

# Find the minimum, maximum, and sum of passenger ages
age_min = df_titanic['age'].min()
age_max = df_titanic['age'].max()
age_sum = df_titanic['age'].sum()

print("\nAge statistics from Titanic dataset:")
print(f"Min Age: {age_min}")
print(f"Max Age: {age_max}")
print(f"Sum of Ages: {age_sum}")

# 3. From movie.csv: Identify the director with the highest total director_facebook_likes.
df_movie = pd.read_csv('movie.csv')

# Calculate the total director_facebook_likes by each director
director_likes = df_movie.groupby('director')['director_facebook_likes'].sum()

# Find the director with the highest total director_facebook_likes
top_director = director_likes.idxmax()
top_director_likes = director_likes.max()

print("\nDirector with the highest total director_facebook_likes:")
print(f"Director: {top_director}, Likes: {top_director_likes}")

# Find the 5 longest movies and their respective directors
longest_movies = df_movie[['title', 'duration', 'director']].nlargest(5, 'duration')
print("\nTop 5 longest movies with directors:")
print(longest_movies)

# 4. From Flights parquet file: Check for missing values in the dataset. Fill missing values in a numerical column with the column’s mean.
df_flights = pd.read_parquet('Flights.parquet')

# Check for missing values in the dataset
missing_values = df_flights.isnull().sum()
print("\nMissing values in the Flights dataset:")
print(missing_values)

# Fill missing values in a numerical column (e.g., 'departure_delay') with the column's mean
if 'departure_delay' in df_flights.columns:
    departure_delay_mean = df_flights['departure_delay'].mean()
    df_flights['departure_delay'].fillna(departure_delay_mean, inplace=True)
    print("\nMissing values in 'departure_delay' have been filled with the mean.")

