import math as np

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

vectorized_conversion = np.vectorize(fahrenheit_to_celsius)

# Array of temperatures in Fahrenheit
temperatures_f = np.array([32, 68, 100, 212, 77])

# Convert to Celsius
temperatures_c = vectorized_conversion(temperatures_f)

print(temperatures_c)
