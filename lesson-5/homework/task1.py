def convert_cel_to_far(celsius):
    return round((celsius * 9 / 5) + 32, 2)

def convert_far_to_cel(fahrenheit):
    return round((fahrenheit - 32) * 5 / 9, 2)


def main():
    try:
        
        far = float(input("Enter a temperature in degrees F: "))
        celsius = convert_far_to_cel(far)
        print(f"{far:.2f} degrees F = {celsius:.2f} degrees C\n")
        cel = float(input("Enter a temperature in degrees C: "))
        fahrenheit = convert_cel_to_far(cel)
        print(f"{cel:.2f} degrees C = {fahrenheit:.2f} degrees F")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()
