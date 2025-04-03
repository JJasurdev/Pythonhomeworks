# Load the movie dataset
df_movie = pd.read_csv('movie.csv')

# Group by color and director_name and calculate the total num_critic_for_reviews and average duration
df_grouped_movie = df_movie.groupby(['color', 'director_name']).agg(
    total_reviews=('num_critic_for_reviews', 'sum'),
    avg_duration=('duration', 'mean')
).reset_index()

# Display the result
print("\nMulti-level Grouping on Movie Data:")
print(df_grouped_movie)
