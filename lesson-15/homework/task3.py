import numpy as np
import matplotlib.pyplot as plt

# Generate x values
x = np.linspace(0, 2 * np.pi, 400)

# Compute sine and cosine values
y_sin = np.sin(x)
y_cos = np.cos(x)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y_sin, label='$\sin(x)$', color='b', linestyle='-', marker='o', markersize=4)
plt.plot(x, y_cos, label='$\cos(x)$', color='r', linestyle='--', marker='s', markersize=4)

# Customize the plot
plt.xlabel('x-axis', fontsize=12)
plt.ylabel('y-axis', fontsize=12)
plt.title('Sine and Cosine Functions', fontsize=14, fontweight='bold')
plt.axhline(0, color='black', linewidth=1, linestyle='--')  # Add x-axis
plt.axvline(0, color='black', linewidth=1, linestyle='--')  # Add y-axis
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=12)

# Show the plot
plt.show()
