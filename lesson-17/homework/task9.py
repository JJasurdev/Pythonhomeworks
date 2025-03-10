# Load the Flights dataset
df_flights = pd.read_parquet('Flights.parquet')

# Create a pipeline for Flights dataset
def filter_delay(df):
    return df[df['DepDelay'] > 30]

def create_delay_per_hour(df):
    df['Delay_Per_Hour'] = df['DepDelay'] / df['ScheduledDuration']
    return df

# Apply the pipeline using .pipe()
df_flights_pipeline = (df_flights
                       .pipe(filter_delay)
                       .pipe(create_delay_per_hour))

# Display the result
print("\nFlights dataset with pipeline transformations:")
print(df_flights_pipeline[['DepDelay', 'ScheduledDuration', 'Delay_Per_Hour']].head())
