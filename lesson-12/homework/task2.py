import requests
import json
from bs4 import BeautifulSoup

def scrape_laptops():
    """Scrapes laptop data from the Demoblaze website."""
    url = "https://www.demoblaze.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    laptops = []
    laptop_cards = soup.find_all("div", class_="card")
    
    for laptop in laptop_cards:
        name = laptop.find("h4", class_="card-title").text.strip()
        price = laptop.find("h5").text.strip()
        description = laptop.find("p", class_="card-text").text.strip()
        
        laptops.append({
            "name": name,
            "price": price,
            "description": description
        })
    
    return laptops

def save_to_json(laptops, filename="laptops.json"):
    """Saves laptop data to a JSON file."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(laptops, file, indent=4)
    print(f"Laptop data saved to {filename}")

def main():
    laptops = scrape_laptops()
    save_to_json(laptops)

if __name__ == "__main__":
    main()
