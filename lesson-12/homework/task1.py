from bs4 import BeautifulSoup
import statistics

def load_html(file_path):
    """Loads and parses the HTML file."""
    with open(file_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
    return soup

def extract_weather_data(soup):
    """Extracts weather forecast details from the parsed HTML."""
    weather_data = []
    table_rows = soup.find("tbody").find_all("tr")
    
    for row in table_rows:
        columns = row.find_all("td")
        day = columns[0].text.strip()
        temp = int(columns[1].text.strip().replace("°C", ""))
        condition = columns[2].text.strip()
        weather_data.append((day, temp, condition))
    
    return weather_data

def display_weather_data(weather_data):
    """Displays the extracted weather forecast details."""
    print("5-Day Weather Forecast:")
    for day, temp, condition in weather_data:
        print(f"{day}: {temp}°C, {condition}")

def find_hottest_day(weather_data):
    """Finds the day(s) with the highest temperature."""
    max_temp = max(weather_data, key=lambda x: x[1])[1]
    hottest_days = [day for day, temp, condition in weather_data if temp == max_temp]
    print(f"Hottest day(s): {', '.join(hottest_days)} with {max_temp}°C")

def find_sunny_days(weather_data):
    """Finds and prints the days with Sunny weather."""
    sunny_days = [day for day, temp, condition in weather_data if condition == "Sunny"]
    print(f"Sunny days: {', '.join(sunny_days)}")

def calculate_average_temperature(weather_data):
    """Calculates and prints the average temperature for the week."""
    avg_temp = statistics.mean([temp for _, temp, _ in weather_data])
    print(f"Average temperature: {avg_temp:.2f}°C")

def main():
    """Runs all functions in sequence."""
    file_path = "weather.html"
    soup = load_html(file_path)
    weather_data = extract_weather_data(soup)
    display_weather_data(weather_data)
    find_hottest_day(weather_data)
    find_sunny_days(weather_data)
    calculate_average_temperature(weather_data)

if __name__ == "__main__":
    main()
