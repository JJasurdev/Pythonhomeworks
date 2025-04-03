# Load the movie.csv file
df_movie = pd.read_csv('movie.csv')

# Create two smaller DataFrames
df_color = df_movie[['director_name', 'color']]
df_reviews = df_movie[['director_name', 'num_critic_for_reviews']]

# Perform a left join on director_name
df_left_join = pd.merge(df_color, df_reviews, on='director_name', how='left')

# Perform a full outer join on director_name
df_outer_join = pd.merge(df_color, df_reviews, on='director_name', how='outer')

# Count the number of rows in the resulting DataFrames
left_join_rows = df_left_join.shape[0]
outer_join_rows = df_outer_join.shape[0]

print("\nLeft Join - Number of rows:", left_join_rows)
print("Full Outer Join - Number of rows:", outer_join_rows)
