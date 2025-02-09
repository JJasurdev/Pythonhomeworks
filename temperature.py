
def convert_fahrenheit():
    fahrenheit = float(input("Enter the temperature in degrees Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print("The temperature is", celsius, "degrees Celsius.")
            
def convert_celsius():
    celsius = float(input("Enter the temperature in degrees Celsius: "))
    fahrenheit = celsius * 9/5 + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")
    