# Load the movie dataset
df_movie = pd.read_csv('movie.csv')

# Define the function to classify movies based on duration
def classify_movie_duration(duration):
    if duration < 60:
        return 'Short'
    elif 60 <= duration <= 120:
        return 'Medium'
    else:
        return 'Long'

# Apply the function to classify movies and create a new column 'Duration_Category'
df_movie['Duration_Category'] = df_movie['duration'].apply(classify_movie_duration)

# Display the result
print("\nMovie dataset with duration classification:")
print(df_movie[['title', 'duration', 'Duration_Category']].head())

