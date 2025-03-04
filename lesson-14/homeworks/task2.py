import math as np

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

vectorized_conversion = np.vectorize(fahrenheit_to_celsius)

# Array of temperatures in Fahrenheit
temperatures_f = np.array([32, 68, 100, 212, 77])

# Convert to Celsius
temperatures_c = vectorized_conversion(temperatures_f)

print(temperatures_c)

# Task 2: Custom function for power calculation
def power_function(base, exponent):
    return base ** exponent

vectorized_power = np.vectorize(power_function)

# Arrays of numbers and powers
bases = np.array([2, 3, 4, 5])
exponents = np.array([1, 2, 3, 4])

# Compute powers
results = vectorized_power(bases, exponents)

print(results)