# Load the Flights dataset
df_flights = pd.read_parquet('Flights.parquet')

# Ensure 'Year' and 'Month' columns exist, if not, extract them from the 'FlightDate' column (if it exists)
if 'FlightDate' in df_flights.columns:
    df_flights['Year'] = pd.to_datetime(df_flights['FlightDate']).dt.year
    df_flights['Month'] = pd.to_datetime(df_flights['FlightDate']).dt.month

# Group by Year and Month and calculate the required metrics
df_grouped_flights = df_flights.groupby(['Year', 'Month']).agg(
    total_flights=('FlightId', 'count'),
    avg_arrival_delay=('ArrDelay', 'mean'),
    max_departure_delay=('DepDelay', 'max')
).reset_index()

# Display the result
print("\nNested Grouping on Flights:")
print(df_grouped_flights)
