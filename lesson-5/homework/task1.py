def convert_cel_to_far(celsius: float) -> float:
    return round(celsius * 9/5 + 32, 2)

def convert_far_to_cel(fahrenheit: float) -> float:
    return round((fahrenheit - 32) * 5/9, 2)

def main():
    try:
        # Prompt for Fahrenheit to Celsius
        far = float(input("Enter a temperature in degrees F: "))
        celsius = convert_far_to_cel(far)
        print(f"{far} degrees F = {celsius} degrees C\n")

        # Prompt for Celsius to Fahrenheit
        cel = float(input("Enter a temperature in degrees C: "))
        fahrenheit = convert_cel_to_far(cel)
        print(f"{cel} degrees C = {fahrenheit} degrees F")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
