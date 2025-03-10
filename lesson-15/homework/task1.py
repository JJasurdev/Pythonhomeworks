import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return x**2 - 4*x + 4

# Generate x values
x = np.linspace(-10, 10, 400)
y = f(x)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='$f(x) = x^2 - 4x + 4$', color='b', linewidth=2)

# Customize the plot
plt.xlabel('x-axis', fontsize=12)
plt.ylabel('y-axis', fontsize=12)
plt.title('Quadratic Function: $f(x) = x^2 - 4x + 4$', fontsize=14, fontweight='bold')
plt.axhline(0, color='black', linewidth=1, linestyle='--')  # Add x-axis
plt.axvline(0, color='black', linewidth=1, linestyle='--')  # Add y-axis
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=12)

# Show the plot
plt.show()

