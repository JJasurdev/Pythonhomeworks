import sqlite3
import pandas as pd

# 1. Read the 'chinook.db' and display the first 10 rows of the 'customers' table
conn = sqlite3.connect('chinook.db')
df_customers = pd.read_sql_query("SELECT * FROM customers", conn)
print("First 10 rows of customers table:")
print(df_customers.head(10))
conn.close()

# 2. Load the 'iris.json' file into a DataFrame and show shape and column names
df_iris = pd.read_json('iris.json')
print("\nShape of the iris dataset:", df_iris.shape)
print("Columns in the iris dataset:", df_iris.columns)

# 3. Load the 'titanic.xlsx' file into a DataFrame and display the first 5 rows
df_titanic = pd.read_excel('titanic.xlsx')
print("\nFirst 5 rows of Titanic dataset:")
print(df_titanic.head())

# 4. Read the Parquet file into a DataFrame and use info to summarize it
df_flights = pd.read_parquet('Flights.parquet')
print("\nSummary of the Flights dataset:")
print(df_flights.info())

# 5. Load the 'movie.csv' file into a DataFrame and display a random sample of 10 rows
df_movie = pd.read_csv('movie.csv')
print("\nRandom sample of 10 rows from the movie dataset:")
print(df_movie.sample(10))
